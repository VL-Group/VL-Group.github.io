import os
#import cv2
from PIL import Image
import matplotlib.pyplot as plt 

def img_resize(root, shape):
	for file in os.listdir(root):
		if file.split('.')[-1] in ['jpg', 'png']:
			print(file)
			img = Image.open(file).resize(shape).convert('RGB')
			img.save('../' + file.split('.')[0] + '.jpg')
			# plt.imshow(img)
			# plt.savefig( )
			# img = cv2.imread(file)
			# img = cv2.resize(img, shape, interpolation=cv2.INTER_AREA)
			# cv2.imwrite('../' + , img)


img_resize('./', (1100, 600))