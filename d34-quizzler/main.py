from question_model import Question
# from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
import json
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# get new trivia questions:
URL="https://opentdb.com/api.php?amount=10&type=boolean"
params = {
    "amount": "10",
    "type": "boolean"
}
res = requests.get(URL, params=params)
res.raise_for_status()
question_data = res.json()
question_data = question_data["results"]

#print(json.dumps(question_data, indent = 2))

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
