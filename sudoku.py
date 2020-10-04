# Trying to create a sudoku generator
import random
numberIndex = [1,2,3,4,5,6,7,8,9]
blocker = [[],[],[],[],[],[],[],[],[]]

def createBoard():
    global blocker
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


    # Setting the amount of numbers to attempt placing into the board, should probably randomize this between a range
    startNumbers = 60
    tryNumbers = []
    vertList=[]

    # Populate a list of numbers to try placing on the board
    c=0
    while c < startNumbers:
        num = random.randint(1,9)
        if tryNumbers.count(num) <= 9:
            tryNumbers.append(num)
        c+=1

    n=0
    x=0
    y=0
    while x <= 9 or len(tryNumbers) > 0:
        cellSelect = random.randint(0,2)
        y+=cellSelect

        if y >= 9 and x < 8:
            x+=1
            y=cellSelect

        # Get a random number from our list of available nums
        tryNum = random.choice(tryNumbers)
        
        # Check the horizontal for a matching value
        if tryNum in board[x]:
            #tryNum = random.choice(tryNumbers)
            continue    
        
        # Chek the vertical
        if x >= 1 and x <= 8 and y <= 8:
            r=0
            vertList=[]
            while r < 9:
                vert = board[r][y]
                vertList.append(vert)
                r+=1

            if tryNum in vertList:
                continue


        # Hack to check neighboring cells for safety
        # TODO: Fix this, make it better!
        if (x == 0 or x == 1 or x == 2) and (y == 0 or y == 1 or y == 2):
            if tryNum in blocker[0]:
                continue
        elif (x == 0 or x == 1 or x == 2) and (y == 3 or y == 4 or y == 5):
            if tryNum in blocker[1]:
                continue
        elif (x == 0 or x == 1 or x == 2) and (y == 6 or y == 7 or y == 8):
            if tryNum in blocker[2]:
                continue
        elif (x == 3 or x == 4 or x == 5) and (y == 0 or y == 1 or y == 2):
            if tryNum in blocker[3]:
                continue
        elif (x == 3 or x == 4 or x == 5) and (y == 3 or y == 4 or y == 5):
            if tryNum in blocker[4]:
                continue
        elif (x == 3 or x == 4 or x == 5) and (y == 6 or y == 7 or y == 8):
            if tryNum in blocker[5]:
                continue
        elif (x == 6 or x == 7 or x == 8) and (y == 0 or y == 1 or y == 2):
            if tryNum in blocker[6]:
                continue
        elif (x == 6 or x == 7 or x == 8)  and (y == 3 or y == 4 or y == 5):
            if tryNum in blocker[7]:
                continue
        elif (x == 6 or x == 7 or x == 8)  and (y == 6 or y == 7 or y == 8):
            if tryNum in blocker[8]:
                continue

        # Check for an empty cell
        # print(board[x][y])
        if y <= 8 and board[x][y] == 0 and len(tryNumbers) >= 1:

            board[x][y] = tryNum
            del(tryNumbers[tryNum])

            # Hack to populate blocker list with unsafe value lists for each 3x3 grid
            # TODO: Clean this up, make it better.
            if (x == 0 or x == 1 or x == 2) and (y == 0 or y == 1 or y == 2):
                blocker[0].append(tryNum)
            elif (x == 0 or x == 1 or x == 2) and (y == 3 or y == 4 or y == 5):
                blocker[1].append(tryNum)
            elif (x == 0 or x == 1 or x == 2) and (y == 6 or y == 7 or y == 8):
                blocker[2].append(tryNum)
            elif (x == 3 or x == 4 or x == 5) and (y == 0 or y == 1 or y == 2):
                blocker[3].append(tryNum)
            elif (x == 3 or x == 4 or x == 5) and (y == 3 or y == 4 or y == 5):
                blocker[4].append(tryNum)
            elif (x == 3 or x == 4 or x == 5) and (y == 6 or y == 7 or y == 8):
                blocker[5].append(tryNum)
            elif (x == 6 or x == 7 or x == 8) and (y == 0 or y == 1 or y == 2):
                blocker[6].append(tryNum)
            elif (x == 6 or x == 7 or x == 8) and (y == 3 or y == 4 or y == 5):
                blocker[7].append(tryNum)
            elif (x == 6 or x == 7 or x == 8) and (y == 6 or y == 7 or y == 8):
                blocker[8].append(tryNum)

            y+=1
            n+=1
        else:
            y+=1
            break

    return(board)

def createHTML(board):
    web = open("sudoku.html","w")
    web.write("<!DOCTYPE html><html><head><style>")
    web.write("table, td {  border: 1px solid black; border-collapse: collapse; } td { padding:20px;}</style></head><body>")
    web.write("<table>")
    for row in board:
        web.write("<tr>")
        for i in row:
            if i == 0:
                web.write("<td></td>")
            else:
                web.write("<td>{}</td>".format(i))
        web.write("</tr>")
    web.write("</table></body></html>")
    web.close()

#Create a new sudoku board
newBoard = createBoard()
for row in newBoard:
    print(row)

# Output the puzzle to html
createHTML(newBoard)


# Solve the generated puzzle....
numList=[]
x=0
y=0
vertList=[]
horizontalsafe = True
solveBoard = newBoard.copy()
while x < 1:
    
    if y >= 9 and x < 8:
        x+=1
        y=0

    if solveBoard[x][y] == 0:
        print("do something")
        numList = numberIndex.copy()

        # Check the horizontal for safety
        for i in numList:
            if i in solveBoard[x]:
                numList.remove(i)

        # Check block list for unsafe numbers
        for i in numList:
            if i in blocker[x]:
                numList.remove(i)


    print(numList)
    # Increment the main counter        
    y+=1

print("Solving....")
for row in solveBoard:
    print(row)