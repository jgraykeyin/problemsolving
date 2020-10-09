import copy

def rotate(numList):

    # Ran into problems copying the list so ended up using this deepcopy function after digging around stackoverflow
    newList = copy.deepcopy(numList)

    x=0
    y=0
    c=2
    d=0

    # I was originally setting all the values manually but noticed a pattern of incrementing / decrenting values...
    # This could probably be tweaked to handle different sized matrices?
    for row in newList:
        for i in row:
            newList[x][y] = numList[c][d]
            c-=1
            y+=1
            if c < 0:
                c=2

            if y > 2:
                y=0
        d+=1
        x+=1

    # Couldn't figure out how to return the list in rows, so returning the whole list for now
    return newList

matrix = [[1,2,3],[4,5,6],[7,8,9]]

rotatedMatrix = rotate(matrix)
for row in rotatedMatrix:
    print(row)


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
def load_image_to_2d_list(image_path):
    img = mpimg.imread(image_path)
    return [[i for i in row] for row in img]
def show_image_from_2d_list(l):
    plt.imshow(l)
    plt.show()
img_path = "cameraman.jpg"
#show_image_from_2d_list(mpimg.imread(img_path))
show_image_from_2d_list(rotate(load_image_to_2d_list(img_path)))