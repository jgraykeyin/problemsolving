# Trying to create a sudoku generator
import random

numberIndex = [1,2,3,4,5,6,7,8,9]
board = [[0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]
        ]         

startNumbers = 28
tryNumbers = []

c=0
while c < startNumbers:
    num = random.randint(1,9)
    if tryNumbers.count(num) <= 9:
        tryNumbers.append(num)
    c+=1

n=0
x=0
y=0
#add=1
#lastNum = 0
while n < 9:
    # print("n is {}".format(n))
    cellSelect = random.randint(0,2)
    y+=cellSelect

    if y > 8:
        x+=1
        y=cellSelect

    tryNum = random.choice(tryNumbers)
    while tryNum in board[x]:
        # print("{} is already in row".format(tryNum))
        tryNum = random.choice(tryNumbers)
    
    if board[x][y] == 0:
        board[x][y] = tryNum
        # print("Placed {}".format(tryNum))
        del(tryNumbers[tryNum])
        # lastNum = tryNum
        y+=1
        n+=1
    else:
        y+=1
        #print("second break at {}".format(tryNum))
        break



for row in board:
    print(row)