class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.score = 0
        self.question_list = question_bank
        self.num_questions = len(question_bank)

    def next_question(self):
        # ask the user a question
        question_num = self.question_number
        question_list = self.question_list
        question = self.question_list[question_num].question
        answer = self.question_list[question_num].answer
        user_answer = input(f"Q.{question_num +1}: {question}. (True/False)? ")
        self.question_number += 1
        self.check_answer(user_answer, answer)

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def check_answer(self, user_answer, correct_answer):
        if user_answer[0].lower() == correct_answer[0].lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Sorry, that is not correct.")
        print(f"The correct answer is {correct_answer}")
        print(f"your score is: {self.score}/{self.question_number}")
        print("\n")
