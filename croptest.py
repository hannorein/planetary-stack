#!/bin/python
import scipy 
import scipy.ndimage
import glob
for i,fn in enumerate(glob.glob("data/*.jpg")):
    f = scipy.ndimage.imread(fn)
    fc = f[1650:1950,2750:3000]
    scipy.misc.imsave('data_crop/%03d.png'%i, fc) 
    print(i)
