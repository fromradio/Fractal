# test
import numpy as np
import scipy as sp
import cv2
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib import cm

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
        
        self.para = [30,1e20]
        if para:
            self.para = para# iteration and the radius
        self.imageInit()
        
    def imageInit(self):
        self.comArray = np.zeros((self.width,self.height),dtype=np.complex128)
        xlin = np.linspace(0,self.xlen,self.width)
        ylin = np.linspace(0,self.ylen,self.height)
        xv,yv = np.meshgrid(xlin,ylin)
        #xinterval = float(self.xlen)/(self.width-1)
        #yinterval = float(self.ylen)/(self.height-1)
        self.comArray = self.origin[0]+1j*self.origin[1]+xv+1j*yv
        Z = 0*self.comArray
        count = np.zeros((self.width,self.height),dtype = np.int8)
        judgeArray = np.ones((self.width,self.height),dtype = np.bool)
        
        for i in range(0,self.para[0]):
            Z[judgeArray]  =  Z[judgeArray]*Z[judgeArray]+self.comArray[judgeArray]
            func = abs(Z)
            #testF = np.where(func>self.para[1])
            #print testF
            
            count[(judgeArray)&(func>self.para[1])] = i
            judgeArray[func>self.para[1]] = False
            func[func>self.para[1]] = 0
        #func = abs(Z)
        #print func[func<self.para[1]]
        #print func
        #func[func<self.para[1]] = 0
        self.toImage(count)
        #print func
        #print self.comArray
    def toImage(self,func):
        # do log
        print func
        func[func>self.para[1]] = np.log10(func[func>self.para[1]])
        plt.pcolor(func,cmap = cm.cool)
        plt.colorbar()
        plt.show()
    def computeFractal(self):
        pass
#main function for debug
def main():
    fI = fractalImage((-1,-1),0.2,0.2,500,500)
if __name__ == '__main__':
    main()
    