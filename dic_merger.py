import json

def main():
	jsonFile1=input("input json file 1's path")
	jsonFile2=input("input json file 2's path")
	outputFileName=input("outputFileName's path")
	f1=open(jsonFile1)
	f2=open(jsonFile2)
	fout=open(outputFileName,"w")
	dic1=json.loads(f1.read())
	dic2=json.loads(f2.read())
	dicOut=dict(dic1,**dic2)
	json.dump(dicOut,fout)
	f1.close()
	f2.close()
	f2.close()

	
if __name__ == '__main__':
	main()
	
