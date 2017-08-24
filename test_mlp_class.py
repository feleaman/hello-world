import numpy as np
from sklearn.neural_network import MLPClassifier
import sys
from PIL import Image
import os.path
from os import listdir
from os.path import isfile, join
import pickle


filename = 'model_05.pkl'
pik = open(filename, 'rb')
clf = pickle.load(pik)

##############
mypath = r'C:\code\db_test'

filenames = [f for f in listdir(mypath) if isfile(join(mypath, f))]
filenames = sorted(filenames)
filepaths = [join(mypath, filename) for filename in filenames]
num_lines = [filename[filename.index('_')+1] for filename in filenames]

images = [Image.open(filepath).convert(mode='L') for filepath in filepaths]

images_rs = []

for k in range(len(images)):
	images_rs.append(np.array(images[k]).reshape(1, -1)[0])
	# images_rs.append(np.array(images[k], dtype='float').reshape(1, -1)[0])
	
num_lines = np.array(num_lines)
for k in range(len(num_lines)):
	num_lines[k] = int(num_lines[k])
	# num_lines[k] = float(num_lines[k])

##############

acc = 0
for image, num_line in zip(images_rs, num_lines):
	prediction = clf.predict(image)
	print(prediction)
	print(num_line)
	print(type(prediction[0]))
	print(type(num_line))
	if prediction[0] == int(num_line):
		print('!!!!!!!!!!!!!!!!!!!!!!!')
		acc = acc + 1 
print(acc)