import numpy as np
from sklearn.neural_network import MLPClassifier
import sys
from PIL import Image
import os.path
from os import listdir
from os.path import isfile, join
import pickle

mypath = r'C:\code\db'

filenames = [f for f in listdir(mypath) if isfile(join(mypath, f))]
filenames = sorted(filenames)
filepaths = [join(mypath, filename) for filename in filenames]
num_lines = [filename[filename.index('_')+1] for filename in filenames]

images = [Image.open(filepath).convert(mode='L') for filepath in filepaths]

images_rs = []

for k in range(len(images)):
	images_rs.append(np.array(images[k]).reshape(1, -1)[0])
	# images_rs.append(np.array(images[k], dtype='float').reshape(1, -1)[0])
	
# num_lines = np.array(num_lines)
for k in range(len(num_lines)):
	num_lines[k] = int(num_lines[k])
	# num_lines[k] = float(num_lines[k])



# sys.exit()
# Neuronal Network
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
hidden_layer_sizes=(1000, 100), random_state=1, activation='tanh',
tol=1.e-9, verbose=True, max_iter=1000)
clf.fit(images_rs, num_lines)   


pik_filename = 'model_05.pkl'
pik = open(pik_filename, 'wb')
pickle.dump(clf, pik)
pik.close()


sys.exit()

