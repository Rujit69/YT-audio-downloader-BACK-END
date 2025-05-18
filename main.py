import yt_dlp

url = "https://youtu.be/Fj6cr3FO2JI"

ydl_opts = {
    'format': 'bestaudio[ext=m4a]/bestaudio',  # Prefer high-quality M4A
    'outtmpl': 'my_audio.%(ext)s',             # Save as 'my_audio.m4a' or similar
    'postprocessors': []  # Don't use ffmpeg or convert
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])



print("Available audio formats:\n")
for f in formats:
        if f.get('vcodec') == 'none':  # No video = audio only
            abr = f.get('abr', 'N/A')  # Audio bitrate
            ext = f.get('ext')
            format_id = f.get('format_id')
            filesize = f.get('filesize', 'N/A')
            print(f"ID: {format_id} | EXT: {ext} | ABR: {abr} kbps | Size: {filesize}")

