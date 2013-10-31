from PIL import Image
from sklearn.datasets import fetch_lfw_people as LFW
import glob
import matplotlib.pyplot as pl
import numpy as np


# read image to array and convert to grayscale
files = glob.glob("data/*/*.jpg")

#Our variables
grayimg1=[]
grayimg2=[]
i = 0
s = 0
ii = 0

#Splitting the datasets into 2 parts
for img in files[:8]:
    im = np.array(Image.open(img).convert('L')) #convert to grayscale - although it looks like a heat map
    grayimg1.append(im)

for img in files[8:]:
    im = np.array(Image.open(img).convert('L')) #converts to grayscale - although it looks like a heat map
    grayimg2.append(im)


#Sorting the pictures by their sum -> darkest image first and brightest last
grayimg1 = sorted(grayimg1,key=np.sum)
grayimg2 = sorted(grayimg2,key=np.sum)


#Printing as gray
pl.gray()

#First dataset pictures
for im in grayimg1:
	pl.subplot(241+i)
	i += 1
	pl.imshow(im)
	pl.axis('off')

pl.show()

#Second dataset images
for gim in grayimg2:
	pl.subplot(241+s)
	s+=1
	pl.imshow(gim)
	pl.axis('off')

pl.show()


#Greyfaces because Anders wants it ...
#No report on this, but it is exactly the same as the previous two ...
ims = LFW(min_faces_per_person=20)
greyfaces = ims.images[:8]
greyfaces = sorted(greyfaces,key=np.mean)

for g in greyfaces:
	pl.subplot(241+ii)
	ii+=1
	pl.imshow(g)
	pl.axis('off')

pl.show()

