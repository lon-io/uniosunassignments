#Program to extract longtitude,latitude and location of a given data
#Name:AGBOLADE ELIZABETH YETUNDE
# Matric no:EEE/2011/0007
# Course :EEE512 Assignment 1
import os
fileList = []
class earthQuakeData:
    def __init__(self, time, lat, long_, location):
        self.time = time
        self.lat = lat
        self.long_ = long_
        self.location = location
    def getlat(self):
        return self.time

    def getLoc(self):
        return self.location

if __name__ == '__main__':
    fil = open("C:\Users\Agbolade Elizabeth Y\Documents\Agbolade.txt","w")
    with open("C:\Users\Agbolade Elizabeth Y\Documents/2.5_month.csv", "r") as f:
        for each in f.readlines():
            fileList = each.split(",")
            print fileList[0]
            print fileList[1]
            print fileList[2]
            print fileList[13] + fileList[14]
            e = earthQuakeData(fileList[0], fileList[1], fileList[2], fileList[13] + fileList[14])
            fil.write(e.getLoc() + "\n")
        fil.close()
            

