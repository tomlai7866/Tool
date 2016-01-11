import simplejson
import urllib
import urllib2
import time 
import os
import ctypes
Current_Path = os.getcwd()

f1=open(Current_Path+"\\SearchResult.txt.txt","w")
f2=open(Current_Path+"\\MD5File.txt","r")


url = "https://www.virustotal.com/vtapi/v2/file/report"


for i in f2.readlines():
	parameters = {"resource": i,
	"apikey":"1aa9436c1c620535edb3f4feaf7847b5a3a5ee19c5df985d42ef14a366239ae4"}
	data = urllib.urlencode(parameters)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	json = response.read()
	Answer = simplejson.loads(json)
	try:
		f1.write(str(Answer["md5"])+' , '+str(Answer["positives"])+' , '+str(Answer["total"])+' , '+str(Answer["permalink"])+"\n")	
	except :
		f1.write(i.rstrip()+' , '+'NA \t\n')
	time.sleep(16)
ctypes.windll.user32.MessageBoxA(0, "Done", "", 0)