
import random

x_coordinate = [x_coordinate for x_coordinate in range(30)]

def setup():
    size(500,500)
    smooth()
    noStroke()
    myInit()

def myInit():
    for i in range(len(x_coordinate)):
        x_coordinate[i] = random.randint(150,350)

def draw():
    background(50)

    for i in range(len(x_coordinate)):
        fill(20)
        ellipse(x_coordinate[i], 250, 5, 5)
        fill(250, 40)
        ellipse(x_coordinate[i], 250, 10 * i,10 * i)
        
    if mouseX > width/2:
        myInit()
        
    print(max(x_coordinate))
