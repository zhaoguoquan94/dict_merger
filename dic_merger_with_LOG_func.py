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
	logFileName=sys.argv[4]
	f1=open(jsonFile1)
	f2=open(jsonFile2)
	fout=open(outputFileName,"w")
	fLog=open(logFileName,"w")
	dic1=json.loads(f1.read())
	dic2=json.loads(f2.read())
	dicOut=dict(dic1,**dic2)
	fLog.write("add these items \n"+str(time.asctime())+"\n")
	fLog.write("	key{0:26}".format("")+"value"+"\n\n\n")
	for key in dic2:
		if key not in dic1:
			fLog.write("	{0:30}".format(key)+str(dic2[key])+"\n")
			# fLog.write(		key+"+++"+str(dic1[key])+"\n")
	json.dump(dicOut,fout)
	f1.close()
	f2.close()
	fout.close()
	fLog.close()

	
def merge(userJson,serverJson):
	userDict=json.loads(userJson)
	serverDict=json.loads(serverDict)
	userDict=dict(userDict,**serverDict)
	return json.dump(userDict)
def writeToFile():
	pass





if __name__ == '__main__':
	main()
	
