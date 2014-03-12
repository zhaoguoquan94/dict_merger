import json
import os
import time
import merger
import codecs
#this program test the performance of merge() and mergeAndLog() func

path=os.getcwd()
serverJson=[]
for file in os.listdir(path):
	if(file.find("serverJson")!=-1):
		serverJson.append(open(os.path.join(path,file),mode='r',encoding="utf8").read())

#we assume that userJson is empty at the beginning
userJson="{}"

timeBegin=time.time()
for sj in serverJson:
    userJson=merger.merge(userJson,sj)
timeConsumed=time.time()-timeBegin
print("merge "+str(len(serverJson))+" json files,and timeConsumed="+str(timeConsumed))

fout=codecs.open("userJson.json","w","utf8")
fout.write(userJson)
fout.close()
