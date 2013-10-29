""" Dem images zomg """
from sklearn.datasets import fetch_lfw_people as LFW
from skimage.filter import threshold_otsu
from PIL import Image
import glob
import matplotlib.pyplot as pl
import numpy as np

# read image to array and convert to grayscale
files = glob.glob("Images/*")

grayimg=[]
for img in files:
    im = np.array(Image.open(img).convert('L'))
    grayimg.append(im)
print len(grayimg)
   
#Variables needed
i = 0


ims = LFW(min_faces_per_person=20)
grayfaces = ims.images[:8]



#Printing the pictures
pl.gray()

for im in grayfaces:
	#We use this to sort the images by their mean
	#np.mean(im.flatten())

	pl.subplot(241+i)
	i += 1
	pl.imshow(im)
	pl.axis('off')

pl.show()

s=0
print len(grayimg)
for gim in grayimg:
	pl.subplot(241+s)
	s+=1
	pl.imshow(gim)
	
pl.show()