import json
import os
import time
import merger
#this program test the performance of merge() and mergeAndLog() func

path=os.getcwd()
serverJson=[]
for file in os.listdir(path):
	if(file.find("serverJson")!=-1):
		serverJson.append(open(os.path.join(path,file),encoding='utf8').read())

#we assume that userJson is empty at the beginning
userJson="{}"

timeBegin=time.time()
for sj in serverJson:
    userJson=merger.merge(userJson,sj)
timeConsumed=time.time()-timeBegin
print("merge "+str(len(serverJson))+" json files,and timeConsumed="+str(timeConsumed))

fout=open("userJson.json",mode="w",encoding="utf8")
fout.write(userJson)
fout.close()
