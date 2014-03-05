import json
import os
import sys
import time
def main():
	#sys.argv pass the path and then call merge() or mergeAndLog() to union the json data
	userJsonPath=sys.argv[1]
	serverJsonPath=sys.argv[2]
	logPath=sys.argv[3]
	fUserJsonIn=open(userJsonPath)
	fServerJsonIn=open(serverJsonPath)
	userJson=json.loads(fUserJsonIn.read())
	serverJson=json.loads(fServerJsonIn.read())
	fUserJsonIn.close()
	fServerJsonIn.close()
	(userJson,log)=mergeAndLog(userJson,serverJson)

	writeToFile(userJson,log,userJsonPath)
	
def merge(userJson,serverJson):
#return Union of userJson and serverJson
	userDict=json.loads(userJson)
	serverDict=json.loads(serverJson)
	userDict=dict(userDict,**serverDict)
	return json.JSONEncoder().encode(userDict)

def mergeAndLog(userJson,serverJson):
	userDict=json.loads("{}")
	serverDict=json.loads(serverJson)
	userDictNew=dict(userDict,**serverDict)
	log=[]
	for key in serverDict:
		if key not in userDict:
			log.append((key,serverDict[key]))
	log=tuple(log)
	
	return json.JSONEncoder().encode(userDictNew),log
def writeToFile(userJson,log,userJsonPath,logPath):
	fUser=open(userJsonPath,"w")
	fLog=open(logPath,"w")
	json.dump(userJson,userJsonPath)
	fLog.write(str(log))

if __name__ == '__main__':
	main()
	
