from question_model import Question
from data import question_data
from open_trivia_db import question_data_db
from quiz_brain import QuizzBrain

# def question_storage(data_list,Question):
#     question_bank = []
#     for q in data_list:
#         question_bank.append(Question(q["text"],q["answer"]))
#     return question_bank

# print(question_storage(question_data,Question))
#__________________________________________________________________________________________

# question_bank = []
# for question in question_data:
#     question_text = question["text"]
#     question_answer = question["answer"]
#     new_question = Question(question_text,question_answer)
#     question_bank.append(new_question)
#__________________________________________________________________________________________


# OPEN TRIVIA DB - https://opentdb.com/

question_bank = []
for question in question_data_db:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)    


quiz = QuizzBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the Quiz")
print (f"Your final score is {quiz.score}/{quiz.question_number}")