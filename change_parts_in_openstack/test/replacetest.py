import os  
import re  

  
def _rename(old,new):  
    new2=''  
    for i in range(0,len(new),2):  
        a=new[i:i+2]  
        if a!='\xa1@':  
            new2+=a;  
     
    print 'new name =',new2  
    print 'old name =',old  
    if new2!=old:  
        print 'begin to rename',old,new2  
        try:  
            os.rename(old,new2)  
        except WindowsError,e:  
            if str(e)=='[Error 183] ':  
                print 'already have ',new2                 
            else:  
                print str(e)  
          
def excuepath(p,oldname,newname):  
    #传递路径及两个字符串作为参数  
    workdir=p  
    os.chdir(workdir)  
    cwd=os.getcwd()  
    dirs=os.listdir(cwd)  
    old=oldname  
    new=newname  
    for tmp in dirs:  
        path=os.path.join(cwd,tmp)  
        print 'path=',path  
        #如果是文件，修改内容后重命名  
        if os.path.isfile(path):  
           #自己内部的字符串不要替换  
            if tmp[-3:]!='.py':  
                data = open(path).read()  
                #print data                
                data = re.sub(old,new, data)
                print data  
                open(path, 'wb').write(data)  
                newpath=path.replace(old,new)  
                _rename(path,newpath)  
        #如果是路径，重命名后递归     
        elif os.path.isdir(path):  
              
            newpath=path.replace(old,new)  
            _rename(path,newpath)  
            excuepath(newpath,old,new)  
              
  
if __name__=='__main__':  
    old='someString'  
    new='newString'  
    excuepath(os.path.abspath('.'),old,new)     