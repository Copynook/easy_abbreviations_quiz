print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does CAD stands for? ")
if answer.lower() == "computer aided design":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What does RDP stands for? ")
if answer.lower() == "remote desktop protocol":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%.")