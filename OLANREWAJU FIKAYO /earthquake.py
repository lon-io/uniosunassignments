import os
fileList = []
class earthQuakeData:
    def __init__(self, time, lat, long_, location):
        self.time = time
        self.lat = lat
        self.long_ = long_
        self.location = location
    def getLat(self):
        return self.lat
    def getLlong_(self):
        return self.long_

if __name__ == '__main__':
    fil = open("C:\Users\ADEDOYIN\Desktop\New folder\openDOC.txt","w")
    with open("C:\Users\ADEDOYIN\Desktop\Python Class 2\2.5_month.csv", "r") as f:
        for each in f.readlines():
            fileList = each.split(",")
            e = earthQuakeData(fileList[1], fileList[2], fileList[20])
            fil.write(e.getLoc() + "\n")
        fil.close()
       #print fileList
