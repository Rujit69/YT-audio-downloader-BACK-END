from fastapi import FastAPI, Form, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import yt_dlp
import os
import unicodedata

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition"],
)

def sanitize_filename(name):
    # Normalize and remove unsupported characters
    return unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii").replace(" ", "_")

@app.post("/submit-url")
async def receive_url(youtube_url: str = Form(...), background_tasks: BackgroundTasks = None):
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]/bestaudio',
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtube_url, download=True)
            filename = ydl.prepare_filename(info)

        if not os.path.exists(filename):
            raise HTTPException(status_code=404, detail="Downloaded file not found")

        safe_filename = sanitize_filename(os.path.basename(filename))

        def iterfile():
            with open(filename, mode="rb") as file_like:
                yield from file_like

        # Schedule file deletion after response is complete
        background_tasks.add_task(os.remove, filename)

        return StreamingResponse(
            iterfile(),
            media_type="audio/m4a",
            headers={
                "Content-Disposition": f'attachment; filename="{safe_filename}"'
            }
        )

    except yt_dlp.utils.DownloadError as e:
        raise HTTPException(status_code=400, detail=f"Download error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
