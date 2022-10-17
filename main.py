import argparse
import config
import ytdownloader
import os
import subprocess
import converter

def main():
    help = ""
    parser = argparse.ArgumentParser(description = help)
    
    # Download video
    parser.add_argument("-d", "--Download", help = "Download a video from youtube")

    # Play a video
    parser.add_argument("-p", "--Play", help = "Play a video")

    # Set up configuration file
    parser.add_argument("-c", "--config", help="Set configuration")


    args = parser.parse_args()

    # Download the video using the ytdownloader script
    if args.Download:

        # Make directory for downloaded videos
        if not os.path.isdir('VIDEOS'):
            os.makedirs('VIDEOS')

        # Download video
        ytdownloader.download(args.Download)

    # Play a video in the command line
    if args.Play: # argument should be the video name, NO EXTENSION
        video_name = args.Play
        
        # First resize the video to config size
        os.system(f'ffmpeg -i {video_name}.mkv -filter:v scale={config.WIDTH}:-1 -c:a copy {video_name}-{config.WIDTH}.mkv')

        # create temporary directory to for video frames
        if not os.path.isdir('tmp-frames'):
            os.makedirs('tmp-frames')

            # Split video into frames inside this directory
            os.system(f'ffmpeg -i {video_name}-{config.WIDTH}.mkv tmp-frames/%04d.png')

        # Play video
        converter.play()

if __name__ == "__main__":
    main()