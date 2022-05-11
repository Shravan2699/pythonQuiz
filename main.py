from data import question_data
from question_model import Question
from quiz_brain import Quizbrain


question_set = []
questions1 = []
answers1 = []

for question in question_data:
    question_set.append(question)
    questions = question["text"]
    questions1.append(questions)
    answers = question["answer"]
    answers1.append(answers)


quiz = Quizbrain(q_data=question_set,question=questions1,ans=answers1)
quiz.next_question()