# -*- coding: utf-8 -*-
import os

path=raw_input("Path")

f1=open('C:\\Users\\tomlai\\Desktop\\Find_Libs.txt','w')

for dirPath, dirNames, fileNames in os.walk(path):
	for f in fileNames:
		a=os.path.join(dirPath, f)
		if a [-5:] == '.java':
			f1.write(a.split('\\')[-1][:-5]+'\n')
		
'''
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
'''