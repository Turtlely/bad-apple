import argparse
import config
import ytdownloader
import os
import subprocess
import sys
import shutil

def main():
    help = ""
    parser = argparse.ArgumentParser(description = help)
    
    # Download video
    # TODO ADD feature to rename the video once downloaded, youtube videos have inconvenient titles
    parser.add_argument("-d", "--Download", help = "Download a video from youtube")

    # Play a video
    parser.add_argument("-p", "--Play", help = "Play a video")

    # Get arguments
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
        global video_name
        video_name = args.Play
        
        try:
            # First resize the video to config size
            os.system(f'ffmpeg -i {video_name}.mkv -filter:v scale={config.WIDTH}:-1 -c:a copy {video_name}-{config.WIDTH}.mkv')
        except e:
            print(e)
            print("The conversion failed, check your width in config.py")
            os._exit(0)

        # create temporary directory to for video frames
        if not os.path.isdir('tmp-frames'):
            os.makedirs('tmp-frames')
            
            try:
                # Split video into frames inside this directory
                os.system(f'ffmpeg -i {video_name}-{config.WIDTH}.mkv tmp-frames/%04d.png')
            except e:
                print(e)
                print("The frame splitting step failed")
                os._exit(0)

        # Import player, only do this once folders and stuff have been set up
        import converter

        # Play
        converter.play(f'{video_name}-{config.WIDTH}.mkv')

        # Remove frames once done
        shutil.rmtree('tmp-frames')
        
        # Remove resized video once done
        os.remove(f'{video_name}-{config.WIDTH}.mkv')



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Delete the relevant directories
        print('Interrupted')
        try:
            # Remove frames once done
            shutil.rmtree('tmp-frames')
            
            # Remove resized video once done
            os.remove(f'{video_name}-{config.WIDTH}.mkv')
            
            # Gracefully exit
            os._exit(0)
        except e:
            print(e)
            os._exit(0)