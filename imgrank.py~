""" Dem images zomg """
from sklearn.datasets import fetch_lfw_people as LFW
from skimage.filter import threshold_otsu
from PIL import Image
import glob
import matplotlib.pyplot as pl
import numpy as np

# read image to array and convert to grayscale
files = glob.glob("data/*/*.jpg")

grayimg1=[]
grayimg2=[]
i = 0
s = 0

for img in files[:8]:
    im = np.array(Image.open(img).convert('L'))
    grayimg1.append(im)
print len(grayimg1)

for img in files[8:]:
    im = np.array(Image.open(img).convert('L'))
    grayimg2.append(im)
print len(grayimg2)

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
print len(grayimg2)
for gim in grayimg2:
	pl.subplot(241+s)
	s+=1
	pl.imshow(gim)
	pl.axis('off')

pl.show()