import subprocess
import PIL, PIL.Image
import numpy as np


# Grader functions

def imgcompare(f1, f2, threshold=0.001):
    '''Compare image files based on number of different pixels.
        Return true if similar enough'''
    try:
        print("comparing %s %s" % (f1,f2))
        # nasty hack to deal with svgs after the fact
        if f1.endswith(".svg"):
            subprocess.call("convert %s f1.png" % f1, shell=True)
            f1 = "f1.png"
        if f2.endswith(".svg"):
            subprocess.call("convert %s f2.png" % f2, shell=True)
            f2 = "f2.png"
 
        im1 = PIL.Image.open(f1)
        im2 = PIL.Image.open(f2)
        diff = np.array(im1)-np.array(im2)
        print("difference percentage %f" % (np.count_nonzero(diff)/float(diff.size)))
        return np.count_nonzero(diff)/float(diff.size) < threshold
    
    except Exception as e:
        print("IMG except ")
        print(e)
        return False
