import os
import re
import time
def mylistdir(p,f):
    a=os.listdir(p)
    fs=myfind(a,f)
    return(fs)
def myfind(l,p):
    lr=[];
    #print p
    p1=p.replace(".",r"\.")
    p2=p1.replace("*",".*")
    p2=p2+"$"
    for a in l:
        #print a
        if  re.search(p2,a,re.IGNORECASE)==None :
           pass
           #print "pass"
        else:
           lr.append(a)
       #print "append"
    return lr
def filelines(f):
    return(len(open(f).readlines()))
def getfiles():
    src_path="test/"
    filetype=["*.png","*.jpeg"]
    nt=range(len(filetype))
    all=[]
    for i in range(len(filetype)):
        files=mylistdir(src_path,filetype[i])
        for  f in files:
            all.append(src_path+f)
    return(all)