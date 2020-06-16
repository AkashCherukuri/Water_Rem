import cv2
import numpy as np

img = cv2.imread('icon.png',1)
img = np.zeros([24,24,3])
cv2.rectangle(img, (2,4),(21,7), (255,255,255),-1)
cv2.rectangle(img, (2,11),(21,14), (255,255,255),-1)
cv2.rectangle(img, (2,18),(21,21), (255,255,255),-1)
cv2.imshow('img', img)
# a = np.resize(np.where(img==0,0.,255.), [24,24])
_,a = cv2.threshold(img[0:24,0:24,0],0,255,cv2.THRESH_BINARY)
b,g,r = cv2.split(img)
img = cv2.merge([b,g,r,a],4)
cv2.imshow('new', img)
if cv2.waitKey()==ord('q'):
	cv2.destroyAllWindows()
	cv2.imwrite('icon.png', img)