from skimage import color
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import numpy as np
img=mpimg.imread("task2.jpg")
orig=img
img=color.rgb2gray(img)
#plt.imshow(img)
#plt.show()
def laplace(im):
    #laplace
    kernel=np.array([[1,1,1],[1,-8,1],[1,1,1]])
    ker=np.flipud(np.fliplr(kernel))
    output=np.zeros_like(im)
    impad=np.zeros((im.shape[0]+4,im.shape[1]+4))
    impad[2:-2,2:-2]=im
    for x in xrange(im.shape[1]):
        for y in range(im.shape[0]):
            output[y,x]=(ker*impad[y:y+3,x:x+3]).sum()
    return output
def average(im):
    #blur
    kernel=np.ones([25,25])
    ker=np.flipud(np.fliplr(kernel))
    output=np.zeros_like(im)
    impad=np.zeros((im.shape[0]+24,im.shape[1]+24))
    impad[12:-12,12:-12]=im
    for x in xrange(im.shape[1]):
        for y in range(im.shape[0]):
            output[y,x]=(ker*impad[y:y+25,x:x+25]).sum()
    return output
def shor(im):
    #sobel horizontal
    kernel=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    ker=np.flipud(np.fliplr(kernel))
    output=np.zeros_like(im)
    impad=np.zeros((im.shape[0]+4,im.shape[1]+4))
    impad[2:-2,2:-2]=im
    for x in xrange(im.shape[1]):
        for y in range(im.shape[0]):
            output[y,x]=(ker*impad[y:y+3,x:x+3]).sum()
    return output    
def sver(im):
    #sobel vertical
    kernel=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    ker=np.flipud(np.fliplr(kernel))
    output=np.zeros_like(im)
    impad=np.zeros((im.shape[0]+4,im.shape[1]+4))
    impad[2:-2,2:-2]=im
    for x in xrange(im.shape[1]):
        for y in range(im.shape[0]):
            output[y,x]=(ker*impad[y:y+3,x:x+3]).sum()
    return output
def hboost(im):
    #highboost
    kernel=np.array([[-1,-1,-1],[-1,17,-1],[-1,-1,-1]])
    ker=np.flipud(np.fliplr(kernel))
    output=np.zeros_like(im)
    impad=np.zeros((im.shape[0]+4,im.shape[1]+4))
    impad[2:-2,2:-2]=im
    for x in xrange(im.shape[1]):
        for y in range(im.shape[0]):
            output[y,x]=(ker*impad[y:y+3,x:x+3]).sum()
    return output   
#laplace RGB
newimage=laplace(img)
#st=np.array(newimage)
stacim=color.gray2rgb(newimage)
plt.axis("off")
plt.imshow(stacim)
plt.show()
#Blur
neimage=average(img)
plt.axis("off")
plt.imshow(neimage,cmap=plt.get_cmap('gray'))
plt.show()
#horizontal
himage=shor(img)
plt.axis("off")
plt.imshow(himage,cmap=plt.get_cmap('gray'))
plt.show()
#vertical
vimage=sver(img)
plt.axis("off")
plt.imshow(vimage,cmap=plt.get_cmap('gray'))
plt.show()
#highboost
boost=hboost(img)
plt.axis("off")
plt.imshow(boost,cmap=plt.get_cmap('gray'))
plt.show()
#highboost RGB
st2=np.array(himage)
stacim2=np.stack((st2,)*3,-1)
plt.axis("off")
plt.imshow(stacim2)
plt.show()