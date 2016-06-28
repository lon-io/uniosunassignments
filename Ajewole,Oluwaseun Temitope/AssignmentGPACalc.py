class gpa_CPGA(object):
    numberOfCourse = None 
    courseUniit =  None 
    courseScores = None 
    initNumberOfCourse = 0
    initCourseUnit = 0
    totalpoints = 0
    totalCredit = 0
    initTotalpoints = 0
    totalSemester = None
    def getcourse(self):
        self.numberOfCourse = input("Enter the number of courses you registered for the semester : ")
        pass
    def getcourseData(self):
        self.courseUnit = input("Enter the course unit " + str(self.initNumberOfCourse + 1)+ " : ")
        pass
    def getTotalSemesters(self):
        self.totalSemester = input("How many semesters will you like to calculate : ")
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
        print ("This The semester you want to calculate the GPA: ")
        self.getcourse()
        if self.numberOfCourse <= 2:
            print ("You must offer must than four(4) courses in a semester")
        else:
            self.calculateGPA()
        pass

    def calculateGPA(self):
        self.getcourse()
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
            self.calculateGPA()
            initTotalSemesterPoints += self.initTotalpoints
            initTotalSemesterCredit += self.totalCredit
            initTotalSemester  += 1
        cgpa = round ((initTotalSemesterPoints)/(initTotalSemesterCredit),2)
        print cgpa
        pass
                 
              

yourName = gpa_CPGA()

yourName.calculateCGPA()
