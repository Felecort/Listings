
x_coordinate = [x_coordinate for x_coordinate in range(10)]
y_coordinate = [y_coordinate for y_coordinate in range(10)]

def setup():
    size(500, 500)
    smooth()
    noStroke()

    for i in range(len(x_coordinate)):
        x_coordinate[i] = 35 * i + 90

    for j in range(len(y_coordinate)):
        y_coordinate[j] = 405 - 35 * j 

def draw():
    background(50)
    
    for i in range(len(x_coordinate)):
        fill(200, 40)
        ellipse(x_coordinate[i], 250, 15 * i, 15 * i)
        fill(0)
        ellipse(x_coordinate[i], 250, 3, 3)

    for j in range(len(y_coordinate)):
        fill(200, 40)
        ellipse(y_coordinate[j], 320, 15 * j, 15 * j)
        fill(0)
        ellipse(y_coordinate[j], 320, 3, 3)

def keyPressed():
    if key == "s": saveFrame("myProcessing.png")
