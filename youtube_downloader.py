import os
import yt_dlp

def download_youtube_video(video_url):
    try:
        # Get the "Downloads" folder path
        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        
        # Set options for yt_dlp
        ydl_opts = {
            'outtmpl': os.path.join(downloads_folder, '%(title)s.%(ext)s'),
            'format': 'bestvideo+bestaudio/best'


        }
        
        # Download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        
        print(f"Video downloaded successfully and saved to {downloads_folder}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Input from the user
while True:
    video_url = input("Enter the YouTube video URL (or type 'exit' to quit): ")
    if video_url.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        break
    download_youtube_video(video_url)
