#704 Task 3
#13/09/24
#fatwell
names = []
scores = []
for i in range(5):
    name = input("Enter your name: ")
    names.append(name)
    score = float(input("Enter your test score"))
    while score > 100 or score < 0:
        print("Error this is not a test score between 0 and 100")
        score = float(input("Enter your test score"))
    scores.append(score)
print(scores)
print(names)
