#!/usr/bin/env python3

import cv2
import yt_dlp
from sys import argv
import subprocess


def displayImage(imagePath):
    try:
        subprocess.run(["feh", imagePath])
    except FileNotFoundError:
        print("feh is not installed or not in the PATH.")

def capture_frames(video_id, num_frames=1, output_folder='/home/mr124/Pictures/StocksFrames'):
    video_url = f'https://www.youtube.com/watch?v={video_id}'

    ydl_opts = {'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'outtmpl': 'video.%(ext)s',
                'quiet': True  # Add this option to suppress output
                }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        video_url = info_dict['url']

    cap = cv2.VideoCapture(video_url)

    print(f"Video Stream Properties: {cap.get(cv2.CAP_PROP_FRAME_WIDTH)} x {cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}")

    frame_count = 0

    while frame_count < num_frames:
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture frame. Check video URL or stream.")
            break

        frame_count += 1
        
        # Save the frame to the output folder
        frame_filename = f'{output_folder}/frame_{frame_count}.jpg'
        cv2.imwrite(frame_filename, frame)
        return frame_filename

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        video_id=argv[1]
        framePath = capture_frames(video_id, num_frames=1)
        displayImage(framePath)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cv2.destroyAllWindows()
