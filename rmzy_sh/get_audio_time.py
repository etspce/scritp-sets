#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/8/8 15:54
# @Author  : Xzx
# @FileName: get_audio_time.py
# @Software: PyCharm
import librosa                                      #pip install librosa
file_url = "../baidu_sh/audio/wg_0235/10.m4a"                        #音频文件路径
time = librosa.get_duration(path=file_url)
print(time)