###Useage:  in command line
#python3 testSingleMerge [userJsonFile] [serverJsonFile] [outputFile]

import json
import os
import sys
import time
def main():

	jsonFile1=sys.argv[1]
	jsonFile2=sys.argv[2]
	outputFileName=sys.argv[3]
	f1=open(jsonFile1)
	f2=open(jsonFile2)
	userJson=f1.read()
	serverJson=f2.read()
	f1.close()
	f2.close()
	timeBegin=time.time()
	userJson=merge(userJson,serverJson)
	timeConsumed=time.time()-timeBegin
	print("merge 1 json file"+sys.argv[2]+" and timeConsumed="+str(timeConsumed))
    
	fout=open(outputFileName,mode="w",encoding="utf8")
	fout.write(userJson)
	
	fout.close()
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
	
if __name__ == '__main__':
	main()
	
