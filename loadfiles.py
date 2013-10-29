from PIL import Image
import pylab as pl
import glob
import numpy as np


# read image to array and convert to grayscale
files = glob.glob("Images/*")

grayimg=[]
for img in files:
    im = np.array(Image.open(img).convert('L'))
    grayimg.append(im)
print len(grayimg)
   
i=0
pl.gray() #don't use color for showing images 
axis=('off')
 
for gim in grayimg:
    print grayimg
    pl.subplot(241+i)
   # i += 1
    pl.imshow(gim)

pl.show()
"""
# hist(im.flatten()256)


pl.gray()
pl.figure()
pl.imshow(im)
pl.show()
"""
