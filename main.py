import quiz_brain
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# for i in range(len(question_data)):
#     q = question_data[i]['text']
#     a = question_data[i]['answer']
#     question = Question(q,a)
#     question_bank.append(question.text)

question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

print(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You have completed the quiz\nYour Final Score is: {quiz.score}/{quiz.question_number}")
