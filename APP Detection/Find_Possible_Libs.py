# -*- coding: utf-8 -*-
import os
import re
import shutil

path=raw_input("Path")

f1=open('C:\\Users\\tomlai\\Desktop\\New\\Find_Libs.txt','w')
pat=r'Lcom/[a-zA-z0-9\/]+'
zz=[]
with open(path,'rU') as f3:
	for c in f3.readlines():
		m=re.findall(pat,c)
		if m:
			for i in m:
				if i not in zz:
					zz.append(i)
for i in zz:
	f1.write(i+'\n')
