import random

board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

numList = [1,2,3,4,5,6,7,8,9]
while True:

    if numList == []:
        break
    else:
        num = random.choice(numList)
        positionX = random.randint(0,2)
        positionY = random.randint(0,2)

        try:
            if board[positionX][positionY] == 0:
                board[positionX][positionY] = num
                numList.remove(num)
        except:
            break

for row in board:
    print(row)

print("Chosen number: {}".format(num))
print("Position: {},{}".format(positionX,positionY))
print("Numlist: {}".format(numList))
