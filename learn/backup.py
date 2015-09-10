#!/usr/bin/env python
# coding=utf-8
# Filename: backup.py

import os, time
import tarfile

source = ["/home/erazer/www/enNercms", "/home/erazer/www/player"]
target_dir = "/home/erazer/backup"
today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

if not os.path.exists(today):
    os.mkdir(today)

comment = input("Please input a comment-->")
if len(comment) == 0:
    target = today + os.sep + now + '.tar.gz'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.tar.gz'

tar = tarfile.open(target, "w:gz")

for file in source:
    # 这里增加文件时会把文件本身的路径也加上去
    tar.add(file)

tar.close()

