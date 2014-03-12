import json
import os
import sys
import time
import codecs
def merge(sourceJSON,patchJSON):
	"""return Union of sourceJSON and patchJSON.

Args:
	sourceJSON:origin json which need to patch.
	patchJSON:json that need to be added to sourceJSON.
	"""
	if sourceJSON=="":
		sourceJSON="{}"
	if patchJSON=="":
		patchJSON="{}"
	sourceDict=json.loads(sourceJSON)
	patchDict=json.loads(patchJSON)
	sourceDict=dict(sourceDict,**patchDict)
	return json.JSONEncoder().encode(sourceDict)
def mergeAndLog(sourceJSON,patchJSON):
	"""return Union of sourceJSON and patchJSON as well as a tuple consist of new json key-value pairs added.

Args:
	sourceJSON:origin json which need to patch.
	patchJSON:json that need to be added to sourceJSON.
	"""
	sourceDict=json.loads(sourceJSON)
	patchDict=json.loads(patchJSON)
	sourceDictNew=dict(sourceDict,**patchDict)
	log=[]
	for key in patchDict:
		if key not in sourceDict:
			log.append((key,patchDict[key]))
	log=tuple(log)
	return json.JSONEncoder().encode(sourceDictNew),log
def writeToFile(sourceJSON,log,sourceJSONPath,logPath):
	"""write sourceJSON and log to sourceJSONPath and logPath.

Args:
	sourceJSON:origin json which need to patch.
	log:a tuple consist of new json key-value pairs added. 
	sourceJSONPath:file path that should be write.
	logPath:file path that should be write.
	"""
	fUser=codecs.open(sourceJSONPath,"w","utf8")
	fLog=codecs.open(logPath,"w","utf8")
	json.dump(sourceJSON,sourceJSONPath)
	fLog.write(str(log))
	fUser.close()
	fLog.close()
