import pickle

f=open("C:\\Users\\tomlai\\Desktop\\Python\\virustotal\\virustotal-search.pkl","r")
f1=open("C:\\Users\\tomlai\\Desktop\\Python\\virustotal\\virustotal-search.txt","w")
f2=open("C:\\Users\\tomlai\\Desktop\\Python\\virustotal\\Tryvirustotal.txt","r")

a=pickle.load(f)

#print(type(a))



while True:
	zz=f2.readline()
	if zz == '':
		break
	try:
		f1.write(zz.rstrip()+'\t'+str(a['reports'][zz.rstrip()]['positives'])+'/'+str(a['reports'][zz.rstrip()]['total'])+'\t'+str(a['reports'][zz.rstrip()]['permalink'])+'\n')
	except :
		f1.write(zz.rstrip()+'\t'+'NA \n')

