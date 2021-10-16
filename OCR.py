# Dependencies pip install toch torchvision torchaudio    from PyTorch
# install easyOCR woth command: pip install easyocr
import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np



#  create a variable to save the image path.
IMG_PATH = 'surfe.jpeg'

# start using OCR to recognize what is in an image file.
# 'en' is the language to recognize.
# gpu = False, since I dont need the GPU to support and calculate
reader = easyocr.Reader(['en'], gpu=False)
result = reader.readtext(IMG_PATH)

result

#  this result will give 3 items, location, then the text, then the accuricy "confidance" 
# to plot coordinates to spot where the text is in our Image file
# to visualize open cv need top left and bottom right.

top_left =  tuple(result [0][0][0])
# indexing the first item in result
bottom_right = tuple(result [0][0][2])
text =  result[0][1]
font = cv2.FONT_HERSHEY_SIMPLEX

# to Visualize the result in a bright green color

img = cv2.imread(IMG_PATH)
img = cv2.rectangle(img, top_left, bottom_right, (0,255,0), 5)
img = cv2.putText(img,text, top_left, font, .5, (255,255,255),2,cv2.LINE_AA)
plt.imshow(img)
plt.show()



# #################################################################
# for multiple lines in an IMG_PATH
#  we have to loop over all items in result give them the rectangle and pring the word on it.

img = cv2.imread(IMG_PATH)
for detection in result:
    top_left = tuple([int(val) for val in detection[0][0]])
    bottom_right = tuple([int(val) for val in detection[0][2]])
    text = detection[1]
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.rectangle(img, top_left, bottom_right, (0,255,0), 5)
    img = cv2.putText(img,text, top_left, font, .5, (255,255,255),2,cv2.LINE_AA)

plt.figure(figsize=(10,10))
plt.imshow(img)
plt.show()
