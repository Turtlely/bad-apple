from PIL import Image
import numpy as np
import os
import time

FPS = 24

ascii = ["@","@","%","#","*","+","=","-",":","."," "]

# assign directory
#directory = '../frames'
directory = ''

# iterate over files in
# that directory
for filename in sorted(os.listdir(directory)):
    f = os.path.join(directory, filename)
    #im = np.around(imageio.imread('frames/frame0266.png',as_gray=True)/256, decimals=1)
    try:
        a = Image.open(f).convert('L')
        im = np.around(np.asarray(a)/256, decimals=1)
    except Exception as e:
        print(e)
        continue
    print(f)
    out = [[ascii[int(10*pixel)] for pixel in row] for row in im]

    for row in out:
        for val in row:
            print(val,end=" "),
        print("\n",end="")
    time.sleep(1/FPS)

