import os
import re

path=raw_input("Path")
f1=open('C:\\Users\\tomlai\\Desktop\\Python\\Test\\Find_SQLite.txt','w')
f2=open('C:\\Users\\tomlai\\Desktop\\Python\\Test\\Find_ID.txt','w')
f3=open('C:\\Users\\tomlai\\Desktop\\Python\\Test\\zz\\11MOBILE_DB_V3.sqlite','rU')
pat=r'[A-Z][1-2]\d{8}'

#for i in 


for dirPath, dirNames, fileNames in os.walk(path):
	for f in fileNames:
		a=os.path.join(dirPath, f)
		with open(a,'rU') as f3:
			for c in f3.readlines():
				if c[:6] == 'SQLite':
					f1.write(a+'\n')
				m=re.search(pat,c)
				if m:
					f2.write(m.group()+'\n')