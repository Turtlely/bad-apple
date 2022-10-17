# Imports
from PIL import Image
import numpy as np
import os
import subprocess
import time
import config

# Video Duration function
def get_length(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return float(result.stdout)

# Get file name format from tmp-frames
file_length = len(os.listdir('tmp-frames')[0].rsplit( ".", 1 )[ 0 ])

# Function to display an image onto the command line
def displayFrame(f):
    ascii = config.asciiBD
    try:
        # Open the file
        a = Image.open(f).convert('L')

        # Load image as numpy array
        im = np.around(np.asarray(a)/256, decimals=1)

        # Log the image
        #print(f)

        # Create new array with characters instead of brightnesses
        out = [[ascii[int((len(ascii)-1)*pixel)] for pixel in row] for row in im]

        # mildly inefficient double for loop here, could be optimized lol
        for row in out:
            for val in row:
                print(val,end=" "),
            print("\n",end="")
    
    # If error occurs, just skip the frame
    except Exception as e:
        print(e)

# TODO implement escape key to delete files

# Function to select what images to display on the command line
def play(video_name):
    # Duration of the video
    DURATION_SECONDS = int(get_length(video_name))

    # create sorted list of files to choose from
    files = sorted(os.listdir('tmp-frames'))

    # Number of files
    num = len(files)

    print(num)

    # Get start time
    START = time.time()

    # Variable to store current frame
    current_frame = 1

    # Variable to store previous frame
    old_frame = 0

    # Enter loop until the last frame has been played
    while current_frame <= num:
        # Get frame
        f = os.path.join('tmp-frames', f"{str(current_frame).zfill(file_length)}.png")

        # ONLY display if a frame has changed
        if old_frame < current_frame:
            displayFrame(f)
        
        # Calculate new frame number
        elapsed = time.time()-START

        # Calculate percent elapsed
        percent = elapsed/DURATION_SECONDS

        # Frame number calculation
        old_frame = current_frame
        current_frame = int(percent * num) 