import json
import os
import time
#this program test the performance of merge() and mergeAndLog() func
def merge(userJson,serverJson):
#return Union of userJson and serverJson
	userDict=json.loads(userJson)
	serverDict=json.loads(serverJson)
	userDict=dict(userDict,**serverDict)
	return json.JSONEncoder().encode(userDict)

def mergeAndLog(userJson,serverJson):
	userDict=json.loads(userJson)
	serverDict=json.loads(serverJson)
	userDictNew=dict(userDict,**serverDict)
	log=[]
	for key in serverDict:
		if key not in userDict:
			log.append((key,serverDict[key]))
	log=tuple(log)

path=os.getcwd()
serverJson=[]
for file in os.listdir(path):
	if(file.find("serverJson")!=-1):
		serverJson.append(open(os.path.join(path,file),encoding='utf8').read())

#we assume that userJson is empty at the beginning
userJson="{}"

timeBegin=time.time()
for sj in serverJson:
    userJson=merge(userJson,sj)
timeConsumed=time.time()-timeBegin
print("merge "+str(len(serverJson))+" json files,and timeConsumed="+str(timeConsumed))

fout=open("userJson.json",mode="w",encoding="utf8")
fout.write(userJson)
fout.close()
