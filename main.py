from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import yt_dlp
from yt_dlp.utils import DownloadError

app = FastAPI()

# Optional: Allow frontend to access API (adjust origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with specific frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/submit-url")
async def receive_url(youtube_url: str = Form(...)):
    ydl_opts = {
    'format': 'bestaudio[ext=m4a]/bestaudio',  # Prefer high-quality M4A
    'outtmpl': 'my_audio.%(ext)s',             # Save as 'my_audio.m4a' or similar
    'postprocessors': [] , # Don't use ffmpeg or convert
    'quiet': True   
}
    try:
     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
         ydl.download([youtube_url])
     return {"status": "success", "message": "Download completed"}
    
    except DownloadError as e:
        return {"status": "error", "message": f"Download error: {str(e)}"}
    
    except Exception as e:
        return {"status": "error", "message": f"Unexpected error: {str(e)}"}
    # Do something with the URL (e.g., print, process, or download)
   
    
   













































#! format and size checker not implemented currently
# print("Available audio formats:\n")
# for f in formats:
#         if f.get('vcodec') == 'none':  # No video = audio only
#             abr = f.get('abr', 'N/A')  # Audio bitrate
#             ext = f.get('ext')
#             format_id = f.get('format_id')
#             filesize = f.get('filesize', 'N/A')
#             print(f"ID: {format_id} | EXT: {ext} | ABR: {abr} kbps | Size: {filesize}")

