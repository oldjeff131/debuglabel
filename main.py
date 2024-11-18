import time
import MySQLdb

class Myclass:
    def timer(self):
        self.localtime=time.asctime(time.localtime(time.time()))
        self.timetext=time.strftime("%H%M%S",time.localtime())
        self.daytext=time.strftime("%Y%m%d",time.localtime())

    def filemake(self):
        file=open(self.daytext+self.timetext+".txt","r")
        while():
            file.write()
        file.close()
    
    def textlist():
        a=1



