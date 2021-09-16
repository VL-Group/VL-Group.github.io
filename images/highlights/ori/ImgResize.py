import os
import cv2


def img_resize(root, shape):
	for file in os.listdir(root):
		if file.split('.')[-1] in ['jpg', 'png']:
			img = cv2.imread(file)
			img = cv2.resize(img, shape, interpolation=cv2.INTER_AREA)
			cv2.imwrite('../' + file, img)


img_resize('./', (1500, 700))