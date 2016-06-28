""" NAME :        ADEBAYO AUGUSTINE KEHINDE
    MATRIC NO:    EEE/2011/0002
    LEVEL:        500L
    COURSE CODE:  EEE512            """

class gpa_CPGA(object):
    numberOfCourse = None 
    courseweight =  None 
    courseScores = None 
    initNumberOfCourse = 0
    initCourseweight = 0
    totalpoints = 0
    totalCredit = 0
    initTotalpoints = 0
    totalSemester = None
    
    def getcourse(self):
        self.numberOfCourse = input("Enter the number of courses you have registered for the semester : ")
        pass
    def getcourseData(self):
        self.courseUnit = input("Enter the weight of course " + str(self.initNumberOfCourse + 1)+ " : ")
        pass
    def getTotalSemesters(self):
        self.totalSemester = input("How many semesters will you like to calculate cgpa for: ")
        pass
    def getCourseGrad(self):
        self.courseScores = raw_input("Enter the grade of the course : ")
        self.x  = (self.courseScores).upper()
        pass
    def getCourseRating(self):
        rating = {"A":5,"B":4,"C":3,"D":2,"E":1,"F":0}
        self.y = rating[self.x]
        pass
    def gpa(self):
        print ("This is the semester you want to calculate the GPA: ")
        self.getcourse()
        if self.numberOfCourse <=4 :
            print ("You must offer must than four(4) courses in a semester")
        else:
            self.calculateGPA()
        pass  

    def calculateGPA(self):
        while self.initNumberOfCourse < self.numberOfCourse:
            self.getcourseData()
            self.initCourseUnit = self.courseUnit
            self.totalCredit +=    self.initCourseUnit
            self.getCourseGrad()
            self.getCourseRating()
            self.initTotalpoints += (self.y)* (self.initCourseUnit)
            self.initNumberOfCourse += 1
        gpa = round((self.initTotalpoints)/(self.totalCredit),2)
        self.initNumberOfCourse = 0
        print gpa
        pass
    
    def calculateCGPA(self):
        initTotalSemester = 0
        initTotalSemesterPoints = 0
        initTotalSemesterCredit = 0
        self.getTotalSemesters()
        while initTotalSemester  <  self.totalSemester  :
            print("Enter your grades and the couse unit  for semester " + str(initTotalSemester+1) + ":")
            self.getcourse()
            self.calculateGPA()
            initTotalSemesterPoints += self.initTotalpoints
            initTotalSemesterCredit += self.totalCredit
            initTotalSemester  += 1
        cgpa = round ((initTotalSemesterPoints)/(initTotalSemesterCredit),2)
        print cgpa
        pass
       
        
            
         
        
      

augustine = gpa_CPGA()

augustine.calculateCGPA()  
           
      
            
            
            
            
            
        
            
        
        


























