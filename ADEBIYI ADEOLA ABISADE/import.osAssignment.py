#Adebiyi, Adeola Abisade
#EEE/2011/0003
#Assignment3: Import Os
import os
fileList = []
class earthQuakeData:
    def __init__ (self, time, lat, long_, location):
        self.time = time
        self.lat = lat
        self.long_ = long_
        self.location = location
    def getTime(self):
        return self.time

    def getLoc(self):
        return self.location
if __name__ == '__main__':
    fil = open("C:\Users\ADEOLA PC\Desktop\RAIN\openDOC.txt",'w')
    with open("C:\Users\ADEOLA PC\Desktop\RAIN/2.5_month.csv") as f:
        for each in f.readlines():
            fileList = each.split(",")
            print fileList[0]
            print fileList[1]
            print fileList[2]
            print fileList[13] + fileList[14]
            e = earthQuakeData(fileList[0], fileList[1], fileList[2], fileList[13] + fileList[14])
            fil.write(e.getLoc() + "\n")
        fil.close()
