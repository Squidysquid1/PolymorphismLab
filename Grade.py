# Author:  <Your Name Here>
# Date:    MM/DD/YYYY
# Program: Grade.py
# Descr:
# Definition of superclass GradedActivity
# and subclass FinalExam.

# class to represent a general graded activity
# consisting of a private score out of 100
class GradedActivity:
    # mutator (aka setter) method for private data
    def setScore(self, s):
        self.__score = s

    # accessor (aka getter) method for private data
    def getScore(self):
        return self.__score

    # calculation method to determine grade based upon score
    def getGrade(self):
        if self.__score >= 90:
            grade = 'A'
        elif self.__score >= 80:
            grade = 'B'
        elif self.__score >= 70:
            grade = 'C'
        elif self.__score >= 60:
            grade = 'D'
        else:
            grade = 'F'
        return grade
 
# inherited class to represent a specific type of
# graded activity, a FinalExam, that includes
# additional fields for number of questions
# and number of questions missed

# Python NOTE: By writing GradedActivity inside parentheses after the class name,
# the FinalExam class extends the GradedActivity class (GradedActivity is the
# superclass and FinalExam is the subclass)
class FinalExam(GradedActivity):
	# constructor (Python initializer)
    def __init__(self, questions, missed):
        # set private members
        self.__numQuestions = questions
        self.__numMissed = missed
        # calculate pointsEach assuming maximum 100 points
        self.__pointsEach = 100.0/questions
        # determine score
        numericScore = 100.0 - (missed * self.__pointsEach)
        # set score by calling inherited method
        self.setScore(numericScore)

    # accessor methods
    def getPointsEach(self):
        return self.__pointsEach

    def getNumMissed(self):
        return self.__numMissed
