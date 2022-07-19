from question_model import Question
import data
from quiz_brain import QuizBrain

questions = []
quiz = QuizBrain()

for line in data.question_data:
    questions.append(Question(line['text'], line['answer']))

for question in questions:
    quiz.ask_question(question)
