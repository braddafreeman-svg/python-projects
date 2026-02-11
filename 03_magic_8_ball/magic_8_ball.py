import random

name = "Jake"
question = "Is the future looking bright?"
random_number = random.randint(1, 12)
#print(random_number)

answer = ""
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "If you work hard"
elif random_number == 11:
  answer = "Only if you're happy"
elif random_number == 12:
  answer = "I'm bored of your questions"
else:
  answer = "Error"

if question == "":
  print("You've forgotten to ask something, you doughnut!")
elif name == "":
  print("Question: " + question)
  print("Magic 8-Ball's answer: " + answer)
else:
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)


