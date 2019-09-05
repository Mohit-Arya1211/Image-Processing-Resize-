#Import Libraries

import cv2 
import numpy as np 
import matplotlib.pyplot as plt  

# To display in external window :
# Edit the Image Path when adding a new Image:  
# Format For Adding New Images [ "C://Dir//Folder//Image.jpg" ]

image = cv2.imread(" #For Uploading an Image  ", 1) 


# Resizing the image: 
  
Resized = cv2.resize(image, (255, 255)) 
  
# Heading Array in Output: 

Titles =["Original", "Resized"] 
Resolution =[image.shape, Resized.shape]
images =[image, Resized] 
count = 2
  
for i in range(count): 
    plt.subplot(2, 2, i + 1) 
    plt.title(Titles[i]) 
    plt.imshow(images[i]) 
    plt.title(Resolution[i])
  
plt.show()