from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# make a list of question objects using the database
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# create quizbrain object and feed the question bank into it
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

num_questions = quiz.num_questions
score = quiz.score
print("You've completed the quiz.")
print(f"Your score is {score}/{num_questions}.")
