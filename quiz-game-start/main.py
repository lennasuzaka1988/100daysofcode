from question_model import Question
from data import results
from quiz_brain import QuizBrain


question_bank = []
for question in results:
    question_bank.append(Question(question['question'], question['correct_answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your total score is {quiz.score} / {quiz.question_number}")


# INSTEAD OF:
# points = 0
# for question in range(len(question_bank)):
#     query = input(f"{question_bank[question].text} True or False: ").lower()
#     if query == question_bank[question].answer.lower():
#         print("Correct!")
#         points += 1
#     else:
#         print("Incorrect. Next question!")
