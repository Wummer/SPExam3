""" Dem images zomg """
from sklearn.datasets import fetch_lfw_people as LFW
from skimage.filter import threshold_otsu
import pylab
import numpy as np

#Variables needed
i = 0


pylab.gray()
ims = LFW(min_faces_per_person=20)
print type(ims.images)
grayfaces = ims.images[:8]
print grayfaces
grayfaces.sort()
print grayfaces


for im in grayfaces:
	#We use this to sort the images by their mean
	np.mean(im.flatten())

	pylab.subplot(241+i)
	i += 1
	pylab.imshow(im)
pylab.show()

