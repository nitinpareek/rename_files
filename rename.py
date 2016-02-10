import os
num_list=['0','1','2','3','4','5','6','7','8','9',')','(','[',']','@','#','$','.','_',' ','-','=']
path=input("Enter file path:")
for dirlist,subdir,filelist in os.walk(path):
    for filename in filelist:
        newname=''
        midname=filename
        count=0
        for i in filename:
            try:
                if i in num_list:
                    newname=midname.replace(i,'',1)
                    midname=newname
                    count=1
                else:
                    break
            except:
                print("ERROR")
        
        if count==1:
            try:
                print("(RENAMING)___",filename,'___(TO)___',newname)
                os.rename(dirlist+'/'+filename,dirlist+'/'+newname)
            except FileExistsError:
                pass
        
