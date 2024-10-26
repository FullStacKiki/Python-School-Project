# @title
import random
questions = [
    ("What is the most used database?", "postgresql"),
    ("What is the best javascript library?", "react",),
    ("What is the new progreamming language for backend?", "golang",),
    ("What is the worst database?", "mysql",)]

random.shuffle(questions)

print("In this game if you select the correct answer you gain 10 points, else you will lose 20 points")
total_money = 100
score = 0
for question, answer in questions:
    print(question)
    user_input = input().lower()
    if user_input.lower() == answer:
      score += 1
      total_money += 10
      print("Correct")
    else:
      print("The correct answer was", answer)
      total_money -= 20

print("your total score is", score, "out of", len(questions))
if score > 2:
  print("You have a good perfect knowledge of programming language")
elif score > 1 & score < 3 :
  print("You have a quite good knowledge of programming language")
elif score > 0 & score < 1:
  print("You have a basic knowledge of programming language")
elif score == 0:
  print("You dont know anything about programming")

print("You have a total Credit of", str(total_money) )