import yt_dlp as youtube_dl  # type: ignore

# Replace this URL with the URL of the YouTube video you want to download
video_url = 'https://www.youtube.com/watch?v=aaqp32nPje8'

# Define the download options
ydl_opts = {
    'format': 'best',
    'outtmpl': '%(title)s.%(ext)s',
}

# Download the video
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

print("Download completed!")
