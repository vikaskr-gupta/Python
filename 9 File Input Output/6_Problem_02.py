G = int(input("Enter your score "))

def game():
    return G

score = game()
with open("High_Score.txt", 'r') as f:
    highScoreStr = f.read()

if highScoreStr == '':
    with open("High_Score.txt", 'w') as f:
        f.write(str(score))

elif int(highScoreStr) < score:
    with open("High_Score.txt", 'w') as f:
        f.write(str(score))
