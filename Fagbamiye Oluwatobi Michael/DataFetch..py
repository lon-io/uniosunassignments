import os
import os.path
import time
import sys
import csv



fileList = []
class earthQuakeData:
    def __init__(self,  lat, long_, location):
        self.lat = lat
        self.long_ = long_
        self.location = location
    def getlong(self):
        return self.long_
    def getlat(self):
        return self.lat
    def getLoc(self):
        return self.location

if __name__ == '__main__':
    doc=open("C:\Users\CECILIA O. OWOADE\Desktop\Assignment\openLocation.txt",'w')
    fod =open("C:\Users\CECILIA O. OWOADE\Desktop\Assignment\openLatitude.txt",'w')
    fil = open("C:\Users\CECILIA O. OWOADE\Desktop\Assignment\openLongitude.txt",'w')
    with open(r"C:\Users\CECILIA O. OWOADE\Desktop\Assignment\2.5_month-3.csv",'r') as f:
        for each in f.readlines():
            fileList = each.split(",")
            print fileList
            e = earthQuakeData(fileList[1], fileList[2], fileList[13])
            fil.write(e.getlong() + "\n")
            fod.write(e.getlat() + "\n")
            doc.write(e.getLoc() + "\n")
            


