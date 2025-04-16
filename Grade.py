# Author:  <Your Name Here>
# Date:    MM/DD/YYYY
# Program: Grade.py
# Descr:
# Definition of class GradedActivity.

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