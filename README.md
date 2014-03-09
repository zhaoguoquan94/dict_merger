dict_merger
===========
a merger using python to merge dictionary

2014.3.8 update:
useage:
when you want to merge sourseJson and patchJson,import merger.py like this:

>>>import merger
>>>merger.merge(sourceJson,patchJson)


when you want log as well, type this:

>>>import merger
>>>merger.mergeAndLog(sourceJson,patchJson)

in /test_case we have serverJson1.json to serverJson5.json consist of human-readable json data.
in /test_case we have serverJson6.json to serverJson27.json consist of big json data generated from KeyNote.



old useage
=======================
in command line type

python3 dic_merger.py file1 file2 file3

	file1 is the original json file
	file2 is  dictionary in server
	file3 is output file ,mergered file

Useage:  in command line
python3 testSingleMerge [userJsonFile] [serverJsonFile] [outputFile]
[in]ZGQdeMacBook-Air:test_case user$ python3 testSingleMerge.py userJson.json serverJson2.json userJson.json 
[out]merge 1 json fileserverJson2.json and timeConsumed=0.022077083587646484


###Useage:  in command line
[in]ZGQdeMacBook-Air:test_case user$ python3 testMutiMerge.py 
[output]merge 27 json files,and timeConsumed=0.2748990058898926


==============

python3 dic_merger_with_Log_funv.py file1 file2 file3 file4
	file1:user's json file
	file2:server's json file
	file3:merged json file
	file4:log file,indicating which item has been added