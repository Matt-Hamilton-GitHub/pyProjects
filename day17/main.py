from question_model import Question
from data import question_data
from quiz_brain import Quiz

question_bank = [Question(item['text'], item['answer']) for item in question_data]

userName = input('Please, enter your name: ')
user = Quiz(userName, question_bank)
for _ in user.question_list:
    user.nextQuestion()
user.printScore()