import json
import os
import sys
import time
def main():
	# jsonFile1=input("input json file 1's path")
	# jsonFile2=input("input json file 2's path")
	# outputFileName=input("outputFileName's path")
	jsonFile1=sys.argv[1]
	jsonFile2=sys.argv[2]
	outputFileName=sys.argv[3]
	f1=open(jsonFile1)
	f2=open(jsonFile2)
	fout=open(outputFileName,mode="w",encoding="utf8")
	userJson=f1.read()
	serverJson=f2.read()
	timeBegin=time.time()
	userJson=merge(userJson,serverJson)
	timeConsumed=time.time()-timeBegin
	print("merge 1 json file"+sys.argv[2]+" and timeConsumed="+str(timeConsumed))
	fout.write(userJson)
	f1.close()
	f2.close()
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
	
