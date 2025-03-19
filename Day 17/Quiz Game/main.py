from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

#Convert data into list of questions
question_bank = []
for ques in question_data:
    new_question = Question(text=ques["question"],answer=ques["correct_answer"])
    question_bank.append(new_question)

#Loop through all questions in the question bank list
quiz = QuizBrain(question_bank)
for question in question_bank:
    user_ans = quiz.next_question()
    quiz.check_answer(user_ans)
print(f"Final score: {quiz.score}/{len(question_bank)}")