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

#f1=open(path+'\\Find_SQLite.txt','w')
f2=open(path+'\\Find_ID.txt','w')
pat=[r'[A-Z][1-2]\d{8}',r'09\d{8}',r'\d{4}-\d{4}-\d{4}-\d{4}',
r'\d{4}\s\d{4}\s\d{4}\s\d{4}',r'\w+\@\w+\.\w+',
r'\(0[2-9]{1,3}\)\d{5,8}',
r'0[2-9]{1,3}\-\d{5,8}'
] 

for dirPath, dirNames, fileNames in os.walk(path):
	for f in fileNames:
		a=os.path.join(dirPath, f)
		with open(a,'rU') as f3:
			m=[]
			PathName=''
			for c in f3.readlines():
				if c[:6] == 'SQLite':
					#f1.write(a+'\n')
					shutil.copy(a, afterpath)
				for matchrg in pat:
					m+=re.findall(matchrg,c)
					if PathName=='':
						f2.write('\n'+f+'\n\n')
						PathName=a
			m=sorted({}.fromkeys(m).keys())
			for i in m:
				f2.write(i+'\n')
				
