# test
import numpy as np
import scipy as sp
import cv2


class fractalImage:
    """
    """
    def __init__(self,origin,xlen,ylen,width,height,para = None):
        # origin: (x,y) the point of origin
        # xlen,ylen is the length along x and y direction
        # width and height is the size of the image
        self.origin = origin
        self.xlen = xlen
        self.ylen = ylen
        self.width = width
        self.height = height
        self.imageInit()
        if not para:
            self.para = [10,1000]# iteration and the radius
    def imageInit(self):
        self.comArray = np.zeros((self.width,self.height),dtype=np.complex64)
        xlin = np.linspace(0,self.xlen,self.width)
        ylin = np.linspace(0,self.ylen,self.height)
        xv,yv = np.meshgrid(xlin,ylin)
        #xinterval = float(self.xlen)/(self.width-1)
        #yinterval = float(self.ylen)/(self.height-1)
        self.comArray = self.origin[0]+1j*self.origin[1]+xv+1j*yv
        print self.comArray.shape
        print self.comArray
    def computeFractal(self):
        pass
        
#main function for debug
def main():
    fI = fractalImage((-1,-1),2,2,100,100)
if __name__ == '__main__':
    main()
    