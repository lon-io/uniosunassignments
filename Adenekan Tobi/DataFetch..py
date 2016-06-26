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
        return self.time
    def getlat(self):
        return self.lat
    def getLoc(self):
        return self.location

if __name__ == '__main__':
    doc=open("C:\Users\Oluwatobi.Adenekan\Desktop\PythonClass2\openLocation.txt",'w')
    fod =open("C:\Users\Oluwatobi.Adenekan\Desktop\PythonClass2\openLatitude.txt",'w')
    fil = open("C:\Users\Oluwatobi.Adenekan\Desktop\PythonClass2\openLongitude.txt",'w')
    with open("C:\Users\Oluwatobi.Adenekan\Desktop\PythonClass2\2.5_month.csv",'r') as f:
        for each in f.readlines():
            fileList = each.split(",")
            print fileList
            e = earthQuakeData(fileList[1], fileList[2], fileList[13])
            fil.write(e.getLong() + "\n")
            fod.write(e.getlat() + "\n")
            doc.write(e.getLoc() + "\n")
            fil.close()
            fod.close()
            doc.close()



