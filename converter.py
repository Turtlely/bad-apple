# Imports
from PIL import Image
import numpy as np
import os
import time
import config

# Some basic config things
FPS = 30 # write code to find this automatically
ascii = config.ascii2
DURATION_SECONDS = 219 # write code to find this automatically

# assign directory to get frames from
directory = 'tmp-frames'

# Function to display an image onto the command line
def displayFrame(f):
    try:
        # Open the file
        a = Image.open(f).convert('L')

        # Load image as numpy array
        im = np.around(np.asarray(a)/256, decimals=1)

        # Log the image
        #print(f)

        # Create new array with characters instead of brightnesses
        out = [[ascii[int(10*pixel)] for pixel in row] for row in im]

        # mildly inefficient double for loop here, could be optimized lol
        for row in out:
            for val in row:
                print(val,end=" "),
            print("\n",end="")
    
    # If error occurs, just skip the frame
    except Exception as e:
        print(e)

# Function to select what images to display on the command line
def play():
    # PROCEEDURE: 

    # Start timer
    # Calculate frame number
    # Fetch frame
    # Display frame
    # Repeat

    # create sorted list of files to choose from
    files = sorted(os.listdir(directory))

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
        f = os.path.join(directory, f"{current_frame:04}.png") #May not always be 4 digits, write code to account for this

        # Display the frame
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