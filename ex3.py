from sklearn.datasets import fetch_lfw_people as LFW
from PIL import Image
import pylab
import glob
import numpy
import ImageStat

pylab.gray()


def Rank(path):
 Image_array=[]
 Image_Bri=[]

 if path=='LFW':# Get the image data and Brightness values if images from LFW
    ims=LFW(min_faces_per_person=20)
    for im in ims.images[:8]:
      Image_Bri.append(im.mean())
      Image_array.append(im)
 else:
    Images=glob.glob(path)# Get the image data and Brightness values if images from local folders
    Image_array=[]
    Image_Bri=[]
    for image in Images:
     im=Image.open(image).convert('L')
     Image_Bri.append(ImageStat.Stat(im).mean[0])
     Image_array.append(im)
   
 for key in range(len(Image_Bri)-1):# Rank images according to brightness
    for x in range(len(Image_Bri)-key-1):
       if Image_Bri[x]>Image_Bri[x+1]:
           Image_Bri[x],Image_Bri[x+1]=Image_Bri[x+1],Image_Bri[x]
           Image_array[x],Image_array[x+1]=Image_array[x+1],Image_array[x]

 for i in range(8):# Show re-ranked images
     pylab.subplot(241+i)
     pylab.imshow(Image_array[i])
     pylab.axis('off')
 pylab.show()   


Rank('Imagedata\Images\*.jpg')
Rank('Imagedata\Images2\*.jpg')
Rank('LFW')
    


