# -*- coding: utf-8 -*-
import os
import re
import shutil

keyword=['password','Password']
path=raw_input("Path")

for dirPath, dirNames, fileNames in os.walk(path):
	for f in fileNames:
		a=os.path.join(dirPath, f)
		with open(a,'rU') as f3:
			PathName=''
			for c in f3.readlines():
				for j in keyword:
					if j in c :
						print(c)