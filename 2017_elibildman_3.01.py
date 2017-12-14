import random

answers = ["outlook is good", "ask again later", "yes", "no", "most likely no", "most likely yes",
           "maybe", "outlook is not good"]
print("Magic Eight Ball")
input("Question: ")
print(answers[random.randint(0, len(answers) - 1)])
