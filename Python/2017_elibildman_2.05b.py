print("Welcome to the College Selection Quiz")

colleges = ["Harvard", "MIT", "Brown", "Carnegie Mellon"]
scores = [0, 0, 0, 0]

ans = input("Do you want to go to school in Massachusetts? (y/n): ")
if ans == "y":
    scores[0] += 1
    scores[1] += 1
else:
    scores[2] += 1
    scores[3] += 1

ans = input("Do you want to go to an engineering school? (y/n): ")
if ans == "y":
    scores[1] += 1
    scores[3] += 1
else:
    scores[0] += 1
    scores[2] += 1

ans = input("Do you like theatre? (y/n): ")
if ans == "y":
    scores[3] += 1
else:
    scores[1] += 1
    scores[2] += 1
    scores[0] += 1

print("Final Scores: ")
print(colleges[0] + ": " + str(scores[0]))
print(colleges[1] + ": " + str(scores[1]))
print(colleges[2] + ": " + str(scores[2]))
print(colleges[3] + ": " + str(scores[3]))
