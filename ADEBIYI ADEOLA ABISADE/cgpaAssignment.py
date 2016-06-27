#Adebiyi, Adeola Abisade
#EEE/2011/0003
#Assignment2: To compute CGPA
class gpa(object):
    "To calculate GPA and CGPA"
    arg1 = None
    arg2 = None
    Scale = None
    subData = None
    units = None
    initCourse = 0
    initgetUnits = 0
    totalUnits = 0
    temp = 0
    def getCourse(self):
        #get the number of courses you registered
        self.arg1 = input("Enter the number of course you registered: ")
        pass

    def getSubject(self,value):
        #get the subject value
        self.arg2 = value
        pass

    def getScale(self):
        #To get the scale value
        self.Scale = input("Enter the scale value: ")
        pass

    def getSubjectData(self):
        #get the subject Data
        self.subData = raw_input("Enter your grade for the course: ")
        pass

    def getGradeData(self):
        #use a scale of 5
        self.Scale == 5

        grade = {'a':5, 'b':4, 'c':3, 'd':2, 'e':1, 'f':0}
        x=grade[self.subData]
        return x

    def getUnits(self):
        #get units value
        self.units = input("Enter the units for each course: ")
        pass

    def gpa(self):
        print "Calculate GPA: "
        sem = raw_input("Enter the semester: ")
        self.getScale() #input the scale value
        self.Scale == 5
        self.getCourse()
        if self.arg1 >= 2:
            self.calculateGpa()
        else:
            print "In order to calculate Gpa you should have atleast 2 subject"
        pass

    def calculateGpa(self):
        "To calculate GPA"
        while self.initCourse!=self.arg1:
            self.initCourse=self.initCourse+1
            self.getUnits()
            self.initgetUnits = self.units
            self.getSubjectData()
            self.temp = self.initgetUnits*self.getGradeData()+self.temp
            self.totalUnits=self.totalUnits+self.initgetUnits

        gpa = round((self.temp+.0)/(self.totalUnits+.0),2)
        print "you have registered for total units:"+" "+str(self.totalUnits)+"you have a gpa of:\""+str(gpa)+"\""
        pass

    def cgpa(self):
        print "calculate CGPA"
        semesters = input("Enter the number of semesters: ")
        counter = 0
        tempInit = 0
        tempTotalUnits = 0
        self.getScale()
        self.Scale == 5
        while counter != semesters:
            counter = counter+1
            print "Please enter the details of the semesters"+" "+str(counter)
            self.getCourse()
            self.calculateGpa()
            tempInit = self.temp+tempInit
            tempTotalUnits = tempTotalUnits + self.totalUnits
            self.arg1=0
            self.initCourse=0
            self.temp=0
            self.totalUnits=0
            print "\n"

        cgpa = round((tempInit+.0)/(tempTotalUnits+.0),2)

        print "you have registered for total units:"+" "+str(tempTotalUnits)+" "+"and you have acquired CGPA:\""+str(cgpa)+"\" "
        pass

if __name__ == '__main__':

    Init = gpa()

    Init.cgpa()
    
    
