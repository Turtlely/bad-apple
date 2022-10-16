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

    # Split video into frames
    parser.add_argument("-s", "--Split", help = "Split a video into its frames inside of a folder")
    parser.add_argument("-l", "--List", help = "List available videos to play in terminal")
    parser.add_argument("-p", "--Play", help = "Play a video")
    parser.add_argument("-c", "--config", help="Set configuration")
    args = parser.parse_args()

    if args.Download:
        ytdownloader.download(args.Download)

    if args.Split: # argument should be the name of the video file
        newpath = f'./frames-{args.Split[:-4]}' 
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        subprocess.call(['ffmpeg', '-i', args.Split, f'frames-{args.Split[:-4]}/'+'img%04d.png'])

    if args.Play: # argument should be the folder of the video frames


    print(args.Download)
    # Convert each frame into an ascii frame
    print("working")
    # options:
    # download video
    # play video
    # set config

if __name__ == "__main__":
    main()