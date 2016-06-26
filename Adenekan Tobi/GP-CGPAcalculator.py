class resultChecker(object):
    courseGrade = None
    totalCourseUnits = 0
    totalPointsEarned = 0
    initTotalSemesterPointsEarned = 0
    initTotalSemesterUnits  = 0
    total_CourseOffered = 0
    def __init__(self,total_Semester):
         self.total_Semester = total_Semester
    def getTotalCourseOffered(self):
        self.total_CourseOffered = input("Enter the number of courses you have registered for the semester : ")
        pass
    def getCourseUnit(self):
        self.courseUnit= input("Enter the course Unit : " )
        pass
    def getcourseGrade(self):
        x = raw_input("Enter the grade of your scores : " )
        self.courseGrade = x.upper()
        pass
    def getGradePoints(self):
        rating = {"A":5,"B":4,"C":3,"D":2,"E":1,"F":0}
        self.y = rating[self.courseGrade]
        pass
    def getgpa(self):
        if self.total_CourseOffered <= 2:
            print("You must offer more than two courses in a semester")
        else:
            self.getcalculateGpa()
        pass
    def getcalculateGpa(self):
        self.getTotalCourseOffered()
        for each in range(1,self.total_CourseOffered + 1):
            self.courseUnit= input("Enter the unit of course " + str(each) + " : ")
            self.getcourseGrade()
            self.getGradePoints()
            self.totalCourseUnits += self.courseUnit
            self.PointsEarned =  (self.courseUnit) * (self.y)
            self.totalPointsEarned +=   self.PointsEarned
        gpa = round((self.totalPointsEarned+0)/(self.totalCourseUnits+.0),2)
        print ("Your Gp for this semester is : " + str(gpa))
        pass
    def calculate_CGPA(self):
        for each in range(1, self.total_Semester+1):
            print ("semester : " + str(each))
            self.getcalculateGpa()
            self.initTotalSemesterUnits +=self.totalCourseUnits
            self.initTotalSemesterPointsEarned += self.totalPointsEarned
        cGPA = round(( self.initTotalSemesterPointsEarned+0)/(self.initTotalSemesterUnits +.0),2)
        print ("Your calculated cgpa is : " + str(cGPA))
if __name__ == '__main__':
    print("Enter GP to calculate GP,and Enter CGPA to calculate your CGPA")
    enter = raw_input("What will you like to calculate : ")
    calculator = enter.upper()
    if calculator == "GP" :
        tobi = resultChecker(0)
        tobi.getcalculateGpa()
    elif calculator == "CGPA" :
        y = input("How many semesters will you like to calculate your CGPA : ")
        tobi = resultChecker(y)
        tobi.calculate_CGPA()
    else : print("Please make sure your imputed strings is correct")
        
    
            
            
            
        
    


        
    

        
