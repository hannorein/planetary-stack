#!/bin/python
import scipy 
import scipy.ndimage
from skimage import measure

import glob

fn = "data_crop/004.jpg"

f = scipy.ndimage.imread(fn)
contours = measure.find_contours(r, 0.2)

import matplotlib.pyplot as plt


fig, ax = plt.subplots()
ax.imshow(r, interpolation='nearest', cmap=plt.cm.gray)

for n, contour in enumerate(contours):
    ax.plot(contour[:, 1], contour[:, 0], linewidth=2)

ax.axis('image')
ax.set_xticks([])
ax.set_yticks([])
plt.show()

#for i,fn in enumerate(glob.glob("data_crop/*.jpg")):
#    print(i)
