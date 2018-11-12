from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
img=Image.open("task2.jpg")
im=img.convert('L')
b=np.array(img)
#for y in b:
 #   for x in b[y]:
  #      for i in xrange(3):
   #         b[y][x]=(b[y][x][i]+b[y][x][i+1]+b[y][x][i+2])/3
            
b[600][600][0]=b[600][600][0]+b[600][600][1]+b[600][600][2]
