# -*- coding: utf-8 -*-
import os
import re
import shutil

path=raw_input("Path")
afterpath="C:\\Users\\tomlai\\Desktop\\New"
try:
	os.makedirs(afterpath)
except :
	pass

f1=open(path+'\\Find_SQLite.txt','w')
f2=open(path+'\\Find_ID.txt','w')
pat=[r'[A-Z][1-2]\d{8}',r'09\d{8}',r'\d{4}-\d{4}-\d{4}-\d{4}',
r'\d{4}\s\d{4}\s\d{4}\s\d{4}',r'\w+@\w+\.\w+',r'\d\.\d\.\d\.\d'] 

for dirPath, dirNames, fileNames in os.walk(path):
	for f in fileNames:
		a=os.path.join(dirPath, f)
		with open(a,'rU') as f3:
			PathName=''
			for c in f3.readlines():
				if c[:6] == 'SQLite':
					f1.write(a+'\n')
					shutil.copy(a, afterpath)
				for matchrg in pat:
					m=re.search(matchrg,c)
					if m:
						if PathName=='':
							f2.write(str(f)+'\n\n')
							PathName=a
						f2.write(m.group()+'\n')
			f2.write('\n')
