# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np
import os
import matplotlib.pyplot as plt
import skimage.io as io

images = []
temp = []

file_dir='D:/Anaconda3/spyder/notMNIST/notMNIST_small'
for root, sub_folders, files in os.walk(file_dir):        #读取文件，可以返回根目录，子文件夹，和文件
	for name in files:
		images.append(os.path.join(root,name))
	for name in sub_folders:
		 temp.append(os.path.join(root,name))
for one_folder in temp:
	n_img = len(os.listdir(one_folder))
	print(n_img)
