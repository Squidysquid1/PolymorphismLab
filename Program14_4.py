# Author:  <Your Name Here>
# Date:    MM/DD/YYYY
# Program: Program14_4.py
# Descr:
# In class exercise to demonstrate use of GradedActivity class.

import Grade

def main():
    test = Grade.GradedActivity() # creating an object (aka instance)
    testScore = float(input('Enter a numeric test score.'))
    test.setScore(testScore) # use mutator to set private data
    print('The grade for that test is', test.getGrade())
    
# start program
main()