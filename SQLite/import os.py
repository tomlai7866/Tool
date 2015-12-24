import os
import re
import shutil

afterpath="C:\\Users\\tomlai\\Desktop\\New"
path=raw_input("Path")
f1=open('C:\\Users\\tomlai\\Desktop\\Python\\Test\\Find_SQLite.txt','w')
f2=open('C:\\Users\\tomlai\\Desktop\\Python\\Test\\Find_ID.txt','w')
os.makedirs(afterpath)
pat=r'\w\d{9}'
for dirPath, dirNames, fileNames in os.walk(path):
	for f in fileNames:
		a=os.path.join(dirPath, f)
		with open(a,'r') as f:
			b=f.readline()
			if b[:6] == 'SQLite':
				f1.write(a+'\n')
				shutil.copy(a, afterpath)
			'''
			while b !='':
				if re.search(pat,b):
					f2.write(a+'\n')
					break'''

