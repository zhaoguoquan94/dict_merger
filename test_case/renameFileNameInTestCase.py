import os 
path = "/Users/user/Documents/dict_merger/test_case"
count=0
for file in os.listdir(path): 
    if os.path.isfile(os.path.join(path,file))==True:
        newname="serverJson"+str(count)+".json"
        os.rename(os.path.join(path,file),os.path.join(path,newname)) 
        print (str(file)+'ok')
        count+=1
