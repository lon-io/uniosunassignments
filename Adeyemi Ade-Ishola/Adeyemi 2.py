# Program to solve for CGPA
# Name:Ade-ishola Oluwasegun Adeyemi
# Matric number:EEE/2012/00033
# Course:EEE512 Assignment II

class Gpa(object):
    # data attributes
    "To calculate the Gpa and Cgpa"
    arg1 = None
    arg2 = None
    subData = None
    Scale = None
    credits = None
    initCourse = 0
    initgetCredit = 0
    totalCredits = 0
    temp = 0

    def getCourse(self):
        "get the value of the no of course registered"
        self.arg1 = input("Enter the No of course registered: " )
        pass
    
    def getSubject(self,value):
        "get the subject value"
        self.arg2 = value
        pass
    
    def getScale(self):
        "To get the scale value"
        self.Scale = input("Enter the Scale value :" )
        pass
        
        
    def getSubjectData(self):
        "get the subject Data in string"
        self.subData = raw_input("Enter the grade for each subject: " ) 
        pass              
    def getGradeData(self):
        # To calculate grade for scale,5.0
        scale = 5
        grade = {'A':5,'B':4,'C':3,'D':2,'E':1,'F':0}
        x= grade[self.subData]
        return x 
    def getCredits(self):
        "get credit value"
        self.credits = input("Enter the units for each subject:")
        pass
    
    def gpa(self):
        print "Calculate GPA:"
        sem = raw_input("Enter Semester: " )
        self.getScale() #input the scale value
        if self.Scale == 5:
            self.getCourse()
            if self.arg1 >= 2:
                self.calculateGpa()
            else:
                print "To calculate Gpa you schould have atleast 2 subject minimum"
        else:
            print "you have not entered the scale correctly please try again"
        pass
                
                
    def calculateGpa(self):
        "Method to calculate Gpa "
        while self.initCourse!=self.arg1:
            self.initCourse=self.initCourse+1
            self.getCredits()
            self.initgetCredit = self.credits
            self.getSubjectData()
            #type(self.getSubjectData())
            self.temp = self.initgetCredit*self.getGradeData()+self.temp
            self.totalCredits=self.totalCredits+self.initgetCredit
            
        gpa = round((self.temp+.0)/(self.totalCredits+.0),2)
        print "you have registered for total credits:"+" "+str(self.totalCredits)+" "+"and you have managed a GPA of:\""+str(gpa)+"\""
        pass
    
    def cgpa(self):
        print "Calculate your cgpa: "
        semesters = input("HELLO,Total semesters to be calculated for: " )
        counter = 0
        tempInit = 0
        tempTotalCredits = 0
        self.getScale() #input the scale value
        if self.Scale == 5 or self.Scale == 6:
            while counter != semesters:
                counter = counter+1
                print "Please enter the details of the semester"+" "+str(counter)
                self.getCourse()
                self.calculateGpa()
                tempInit = self.temp+tempInit
                tempTotalCredits = tempTotalCredits + self.totalCredits
                # re-assigning
                self.arg1=0
                self.initCourse =0
                self.temp=0
                self.totalCredits=0
                print "\n"
                
            cgpa = round((tempInit+.0)/(tempTotalCredits+.0),2)
            
            print "you have registered for total credits:"+" "+str(tempTotalCredits)+" "+"and you have acquired CGPA:\""+str(cgpa)+"\" "    
        else:
            print "you have not entered the scale correctly please try again"
        pass


if __name__ == '__main__': # main method
    #how to calculate it

    Init = Gpa() # Creating Instance

    # for calculation of Cgpa (cumulative grade point average)
    Init.cgpa()

    # In Order to calculate Gpa for single semester
    #Init.gpa()


            
