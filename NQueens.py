import random

map = []
def createBoard():
    global map
    map = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
    ]

boardRef = [
    ["a8","b8","c8","d8","e8","f8","g8","h8"],
    ["a7","b7","c7","d7","e7","f7","g7","h7"],
    ["a6","b6","c6","d6","e6","f6","g6","h6"],
    ["a5","b5","c5","d5","e5","f5","g5","h5"],
    ["a4","b4","c4","d4","e4","f4","g4","h4"],
    ["a3","b3","c3","d3","e3","f3","g3","h3"],
    ["a2","b2","c2","d2","e2","f2","g2","h2"],
    ["a1","b1","c1","d1","e1","f1","g1","h1"],
]

createBoard()
queens = []
x=0
y=0
tries=0
z=1
while True:

    x = random.randint(0,7)
    y = random.randint(0,7)

    # print("{},{}".format(x,y))

    if map[x][y] == 0:
        c=0
        z=1
        diagX = 0
        diagY = 0
        while c < 8:
            if map[x][c] == 0:
                map[x][c] = 1
            if map[c][y] == 0:
                map[c][y] = 1

            # Up and Right
            diagX = x - z
            diagY = y + z
            
            if diagX >= 0 and diagY <= 7:
                if map[diagX][diagY] == 0:
                    map[diagX][diagY] = 1

            # Up and Left
            diagX = x - z
            diagY = y - z
            if diagX >= 0 and diagY >= 0:
                if map[diagX][diagY] == 0:
                    map[diagX][diagY] = 1

            # Down and Right
            diagX = x + z
            diagY = y + z
            if diagX <= 7 and diagY <= 7:
                if map[diagX][diagY] == 0:
                    map[diagX][diagY] = 1

            # Down and Left
            diagX = x + z
            diagY = y - z
            if diagX <= 7 and diagY >= 0:
                if map[diagX][diagY] == 0:
                    map[diagX][diagY] = 1
    
            z+=1
            c+=1

        map[x][y] = 2
        queens.append("{}".format(boardRef[x][y]))

    tries = tries + 1

    if tries > 64:
        if len(queens) < 9:
            queens = []
            createBoard()
            tries=0

    if len(queens) == 8:
        break
            
for row in map:
    print(row)

print(queens)
print("Placed {} queens!".format(len(queens)))