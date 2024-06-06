
import os
import time
from prettytable import PrettyTable

class Quiz:

    def __init__(self, userName, quesList):
        self.score = 0
        self.question_list = quesList
        self.question_number = 0
        self.user_name = userName

    def nextQuestion(self):
        print(f"{self.question_number + 1}/{len(self.question_list)}")
        user_answer = input(f"Q.{self.question_number + 1} {self.question_list[self.question_number].question} (True/False)?: ")
        if user_answer.upper() == self.question_list[self.question_number].answer.upper():
            print('Correct!')
            self.question_number += 1      
            self.updateScore()
        else:
            print('Wrong!')
            self.question_number += 1
        
        if self.question_number < len(self.question_list):
            print('Moving to the next question')
        else:
            print("Congrets! You have answered all of the questions!") 

        time.sleep(3)
        os.system('cls')

    def updateScore(self):
        self.score+=1
    def printScore(self):
        table = PrettyTable()
        table.field_names =['User Name', 'Score']
        table.add_row([self.user_name, self.score])
        print(table)