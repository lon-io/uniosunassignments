import os
fileList = []
class earthQuakeData:
    def __init__(self, time, lat, long_, location):
        self.time = time
        self.lat = lat
        self.long_ = long_
        self.location = location
    def getlat(self):
        return self.lat

    def getLoc(self):
        return self.location

    def getLong(self):
        return self.long_

if __name__ == '__main__':
    fil = open("C:\Users\TAIWO\Documents\austin.txt","w")
    with open("C:\Users\TAIWO\Documents/2.5_month.csv", "r") as f:
        for each in f.readlines():
            fileList = each.split(",")
            print fileList[1],fileList[2],fileList[13]
           
            e = earthQuakeData(fileList[0], fileList[1], fileList[2], fileList[13])
            fil.write(e.getlat()+ "\n")
            fil.write(e.getLoc() + "\n")
            fil.write(e.getLong() + "\n")
        fil.close()
            

