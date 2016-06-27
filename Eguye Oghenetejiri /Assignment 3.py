import os
Ass=[]
class earthQuakeData:
    def __init__(self,time,lat_,long_,loc):
        self.time=time
        self.lat_=lat_
        self.long_=long_
        self.loc=loc
    def getLoc(self):
        return self.loc
    
    def getLat(self):
        return self.lat_
    
    def getLong(self):
        return self.long_

if __name__=='__main__':
    fil=open("C:\Users\EGUYE\Documents\openDoc.txt","w")
    with open("C:\Users\EGUYE\Documents\2.5_month.csv","read") as f:
        for each in f.readlines():
            Ass=each.split(',')
            print Ass
            e=earthQuakeData(Ass[20],Ass[1],Ass[2])
            fil.write(e.getLoc(),e.getLat(),e.getLong() +"\n")
        fil.close()
                      
           
