import simplejson
import urllib
import urllib2
import time 

f1=open("C:\\Users\\tomlai\\Desktop\\Python\\virustotal\\virustotal-search.txt","w")
f2=open("C:\\Users\\tomlai\\Desktop\\Python\\virustotal\\Tryvirustotal.txt","r")

url = "https://www.virustotal.com/vtapi/v2/file/report"


for i in f2.readlines():
	parameters = {"resource": i,
	"apikey":"1aa9436c1c620535edb3f4feaf7847b5a3a5ee19c5df985d42ef14a366239ae4"}
	data = urllib.urlencode(parameters)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	json = response.read()
	Answer = simplejson.loads(json)
	print(Answer["md5"])
	try:
		f1.write(str(Answer["md5"])+' , '+str(Answer["positives"])+' , '+str(Answer["total"])+' , '+str(Answer["permalink"])+"\n")	
	except :
		f1.write(i+' , '+'NA \t\n')
	time.sleep(16)
	'''
	try:
		f1.write(zz.rstrip()+' , '+str(a['reports'][zz.rstrip()]['positives'])+' , '+str(a['reports'][zz.rstrip()]['total'])+' , '+str(a['reports'][zz.rstrip()]['permalink'])+'\t\n')
	except :
		f1.write(zz.rstrip()+' , '+'NA \t\n')
	'''