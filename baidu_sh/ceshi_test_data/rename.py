#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/7/18 14:21
# @Author  : Xzx
# @FileName: rename.py
# @Software: PyCharm
import os

# for index, filename in enumerate(os.listdir('C:/Users/issuser/Desktop/img_wg/wg_1/')):  # ‘logo/’是文件夹路径，你也可以替换其他
#     newname = filename.replace(filename, str(index+1) + '.jpg')
#     os.rename('C:/Users/issuser/Desktop/img_wg/wg_1/'+filename, 'C:/Users/issuser/Desktop/img_wg/'+newname)


for index1, filename1 in enumerate(os.listdir('C:/Users/issuser/Desktop/img_wg/wg_2/')):  # ‘logo/’是文件夹路径，你也可以替换其他
    newname1 = filename1.replace(filename1, str(index1+101) + '.jpg')
    os.rename('C:/Users/issuser/Desktop/img_wg/wg_2/'+filename1, 'C:/Users/issuser/Desktop/img_wg/'+newname1)


for index2, filename2 in enumerate(os.listdir('C:/Users/issuser/Desktop/img_wg/wg_3/')):  # ‘logo/’是文件夹路径，你也可以替换其他
    newname2 = filename2.replace(filename2, str(index2+301) + '.jpg')
    os.rename('C:/Users/issuser/Desktop/img_wg/wg_3/'+filename2, 'C:/Users/issuser/Desktop/img_wg/'+newname2)