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

# EXPERIMENTAL RGB FUNCTION
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[39m".format(r, g, b, text)

# Get file name format from tmp-frames
file_length = len(os.listdir('tmp-frames')[0].rsplit( ".", 1 )[ 0 ])

# Function to display an image onto the command line
def displayFrame(f):

    try:
        # Open the file
        a = Image.open(f)

        # For grayscale mode
        if config.COLOR == False:
            # If greyscale, load the greyscale ascii set
            ascii = config.asciiDB

            a = a.convert('L')

            # Load image as numpy array
            im = np.around(np.asarray(a)/256, decimals=1)

            # Create new array with characters instead of brightnesses
            out = [[ascii[int((len(ascii)-1)*pixel)] for pixel in row] for row in im]

            # mildly inefficient double for loop here, could be optimized lol

            # Now this program draws frames as entire frames, no longer pixel by pixel, this makes clearing the screen much much faster
            line = ""

            for row in out:
                for val in row:
                    line += val +" "
                line += "\n"

            print(line)


        # For RGB mode (EXPERIMENTAL)
        else:
            # If RGB, load the RGB ascii set
            ascii = config.RGB

            a = a.convert('RGB')
            
            # Load image as numpy array
            im = np.around(np.asarray(a)/256, decimals=1)

            # mildly inefficient double for loop here, could be optimized lol
            
            # Now this program draws frames as entire frames, no longer pixel by pixel, this makes clearing the screen much much faster
            line = ""

            for row in im:
                for val in row:
                    # Get RGB values
                    b = val[0]
                    r = val[1]
                    g= val[2]

                    # Get brightnesss
                    y = 0.2126 * r + 0.7152 * g + 0.0722 * b

                    # Map brightness to ascii
                    out = ascii[int((len(ascii)-1)*y)]

                    # Print
                    line+=colored(int(r*256), int(g*256), int(b*256), out)+" "

                # Append newline
                line+="\n"

            # Draw frame
            print(line)

    # If error occurs, just skip the frame
    except Exception as e:
        print(e)

# Function to select what images to display on the command line
def play(video_name):
    # Duration of the video
    DURATION_SECONDS = int(get_length(video_name))

    # create sorted list of files to choose from
    files = sorted(os.listdir('tmp-frames'))

    # Number of files
    num = len(files)

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
            # Clear screen
            print(chr(27) + "[2J")
            print(chr(27) + "[1;1f")

            # Display frame
            displayFrame(f)

            # Give time for frame to appear, 0.03 can be changed
            time.sleep(0.025)

        # Calculate new frame number
        elapsed = time.time()-START

        # Calculate percent elapsed
        percent = elapsed/DURATION_SECONDS

        # Frame number calculation
        old_frame = current_frame
        current_frame = int(percent * num) 
