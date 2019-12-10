
import random

x_coordinate = [x_coordinate for x_coordinate in range(30)]

def setup():
    size(500, 500)
    smooth()
    noStroke()
    myInit()

def myInit():
    print("New coordinates: ")
    for i in range(len(x_coordinate)):
        x_coordinate[i] = 250 + random.randint(-100,100)
        print(x_coordinate[i])

def draw():
    background(30)
    for i in range(len(x_coordinate)): 
        fill(20)
        ellipse(x_coordinate[i], 250, 5, 5)
        fill(250, 40)
        ellipse(x_coordinate[i], 250, 10*i, 10*i)
    
    if mouseX > 250:
        myInit()

def keyPressed():
    if key== "s": saveFrame("myProcessing.png")
