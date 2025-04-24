# Author:  <Your Name Here>
# Date:    MM/DD/YYYY
# Program: Program14_4.py
# Descr:
# In class exercise to demonstrate use of GradedActivity class.

import Grade

def main():
    questions = int(input("Enter the number of questions on the exam: "))
    missed = int(input("Enter the number of questions that the students missed: "))
    
    exam = Grade.FinalExam(questions, missed)

    print(f"Each question on the exam counts {exam.getPointsEach()} points.")
    print(f"The exam score is {exam.getScore()}")
    print(f"The exam grade is {exam.getGrade()}")

    
# start program
main()