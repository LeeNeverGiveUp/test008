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
            # print("登录成功！")

        # if "Password is error.(密码错误）" in r.text:
        #     print("登录失败，用户名或者密码不真确，请重新登录！")
        #     continue
        # else:
        #     print("登录成功！")
        #     break
        # except error.URLError as e:
        #     if hasattr(e, 'code'):
        #         print("HTTPError:%d" % e.code)
             
        #     elif hasattr(e, 'reason'):
        #         print("URLError:%s" % e.reason)