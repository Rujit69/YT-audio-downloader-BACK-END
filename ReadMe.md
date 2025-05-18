```md
#YouTube Audio Downloader

![FastAPI](https://img.shields.io/badge/FastAPI-v0.95-green) ![React](https://img.shields.io/badge/React-18-blue) ![Python](https://img.shields.io/badge/Python-3.10-blue) ![yt-dlp](https://img.shields.io/badge/yt--dlp-latest-orange)

A simple and efficient full-stack app to download high-quality YouTube audio (M4A) by providing a YouTube URL.

---

## 🚀 Features

- **Backend:** FastAPI + yt-dlp for fast, reliable YouTube audio extraction and streaming.
- **Frontend:** React app with a clean UI to submit URLs and download audio files.
- **Filename preservation:** Downloads saved with the original YouTube video title.
- **Automatic cleanup:** Temporary files deleted after streaming on the backend.
- **CORS enabled:** Easy connection between frontend and backend.
- Supports drag and drop or URL input (can be added easily).

---

## 📂 Project Structure
```

/backend - FastAPI backend API
/frontend - React frontend app
README.md - This documentation

````

---

## 🔧 Backend Setup

1. Clone repo and go into backend folder:

   ```bash
   cd backend
````

2. Create virtual environment and activate:

   ```bash
   python3 -m venv env
   source env/bin/activate   # Windows: env\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install fastapi uvicorn yt-dlp python-multipart
   ```

4. Run backend server:

   ```bash
   uvicorn main:app --reload
   ```

- API endpoint: `POST http://127.0.0.1:8000/submit-url`
- Form data key: `youtube_url` (string)

---

## ⚛️ Frontend Setup

1. Go into frontend folder:

   ```bash
   cd frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Run frontend:

   ```bash
   npm start
   ```

- Open `http://localhost:3000` in browser.
- Enter YouTube URL and submit.
- Audio file downloads with correct original filename.

---

## 📡 How It Works

1. User enters YouTube URL in frontend.
2. Frontend sends URL to backend `/submit-url` endpoint.
3. Backend uses `yt-dlp` to download best quality audio as M4A.
4. Backend streams the audio file back with `Content-Disposition` header including sanitized filename.
5. Frontend receives file, extracts filename from headers, triggers download with correct name.
6. Backend schedules automatic file deletion after streaming.

---

## 🔑 API Example with curl

```bash
curl -X POST -F "youtube_url=https://www.youtube.com/watch?v=example" http://127.0.0.1:8000/submit-url --output audio.m4a
```

---

## 🧹 Cleanup & Safety

- Filenames sanitized for cross-platform safety.
- Temporary files deleted after streaming using FastAPI BackgroundTasks.
- CORS enabled for frontend/backend communication.

---

## 🛠️ Dependencies

- **Backend:**

  - fastapi
  - uvicorn
  - yt-dlp
  - python-multipart

- **Frontend:**

  - react
  - (Other typical React dependencies)

---

## ⚙️ Deployment Notes

- Backend can be deployed on platforms like Render, Heroku, or AWS Lambda.
- Use ephemeral directories like `/tmp` for downloads if required.
- Frontend can be hosted on Netlify, Vercel, or any static hosting.

---

## 📝 License

MIT License — free to use and modify.

---

Enjoy hassle-free YouTube audio downloads! 🎧🚀

```

---

```
