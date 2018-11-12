from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from skimage import color
im=Image.open("task2.jpg")
im=np.array(im)
#ima=mpimg.imread("task2.jpg")
#im=color.rgb2gray(im)
print im
#print im
print im.shape
#im=np.dot(im[...,:3],[0.299, 0.5870, 0.114])
im=im.convert('L')
print im.shape
plt.imshow(im, cmap=plt.get_cmap("gray"))
plt.axis("off")
plt.show()
kernel=np.zeros([3,3], dtype=int)
kernel[1][1]=-4
kernel[0][1],kernel[2][1],kernel[1][0],kernel[1][2]=1,1,1,1
print kernel
kernel=np.flipud(np.fliplr(kernel))
output=np.zeros_like(im)
impad=np.zeros([im.shape[0]+4,im.shape[1]+4])
impad[2:-2,2:-2]=im
for y in xrange(im.shape[0]):
    for x in xrange(im.shape[1]):
        output[y,x]=(kernel*impad[y:y+3,x:x+3]).sum()
output=np.stack((output,)*3,-1)
plt.imshow(output)
plt.axis("off")
plt.show()
