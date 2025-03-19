class QuizBrain:
    def __init__(self,questions_list):
        """Attributes defined here."""
        self.ques_number = -1
        self.list = questions_list
        self.score = 0

    def next_question(self):
        self.ques_number += 1
        next_ques = self.list[self.ques_number].question
        ans = input(f"Q{self.ques_number + 1}. {next_ques.title()} (True/False) ")
        return ans

    def check_answer(self,ans):
        if ans.lower() == self.list[self.ques_number].answer.lower():
            self.score += 1
            print(f"Correct!\nYour current score is {self.score}\n")
            return True
        print(f"Incorrect! The correct answer is {self.list[self.ques_number].answer}\n")
        return False