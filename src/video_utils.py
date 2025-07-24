import yt_dlp

url = 'https://www.youtube.com/watch?v=1qTLjav3DOw'

ydl_opts = {
    'outtmpl': 'data/videos/%(title)s.%(ext)s', 
    'format': 'best'  # best available quality
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])