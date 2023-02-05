class QuizBrain:
    def __init__(self, question_bank):
        # initialize attributes
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def next_question(self):
        current_answer=self.question_list[self.question_number].text
        correct_answer = self.question_list[self.question_number].answer

        user_answer=input(f'Q.{self.question_number +1}:{current_answer} (True/False)? :')
        self.question_number +=1
        self.check_answer(correct_answer, user_answer)

    def still_has_questions(self):
        return self.question_number< len(self.question_list)

    def check_answer(self,correct_answer,user_answer):

        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"You got it right")
        else:
            print("You got it wrong")
        print(f"The correct answer was {correct_answer  }")
        print(f"Your current score is : {self.score} / {len(self.question_list)}")
        print("\n")