#this moudle is uesd in python3
###Useage:  in command line
#python3 testSingleMerge [userJsonFile] [serverJsonFile] [outputFile]

import json
import os
import sys
import time
import merger
def main():

	jsonFile1=sys.argv[1]
	jsonFile2=sys.argv[2]
	if len(sys.argv)==4:
		outputFileName=sys.argv[3]
	f1=open(jsonFile1)
	f2=open(jsonFile2)
	userJson=f1.read()
	serverJson=f2.read()
	f1.close()
	f2.close()
	timeBegin=time.time()
	userJson=merger.merge(userJson,serverJson)
	timeConsumed=time.time()-timeBegin
	print("merge 1 json file"+sys.argv[2]+" and timeConsumed="+str(timeConsumed))
	if len(sys.argv)==3:
		fout=open(jsonFile1,mode="w",encoding="utf8")
		fout.write(userJson)
	else:
		fout=open(outputFileName,mode="w",encoding="utf8")
		fout.write(userJson)
		fout.close()

if __name__ == '__main__':
	main()
	
