from PIL import Image
import glob
import matplotlib.pyplot as pl
import numpy as np
from sklearn.datasets import fetch_lfw_people as LFW

# get datasets
#Marias fancy machine wants the complete path - just comment that line out and uncomment the next
files = glob.glob("/Users/Maria/Documents/ITandcognition/Github/SPExam3/data/*/*.jpg")
#files = glob.glob("/data/*/*.jpg")
faces = LFW(min_faces_per_person=20)

#print len(faces.images)

#Printing gray
pl.gray()

#Our variables for non-sklearn
grayimg1=[]
grayimg2=[]

#iteration variables
i = 0
s = 0
c = 0

## Sklearn dataset with faces ##

#sorting the faces according to the mean

facessorted = sorted(faces,key=np.mean)

#plotting
for face in facessorted.images[:8]:
	pl.subplot(241+c)
	c+=1
	pl.imshow(face)
	pl.axis('off')
pl.show()

## 2 datasets of random images ##
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
