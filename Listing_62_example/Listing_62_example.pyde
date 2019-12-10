
x_coordinate = [x_coordinate for x_coordinate in range(10)]
print(x_coordinate)
def setup():
    size(500, 500)
    smooth()
    noStroke()
    for i in range(len(x_coordinate)):
        x_coordinate[i] = 35 * i + 90

def draw():
    background(50)
    for i in range(len(x_coordinate)):
        fill(200, 40)
        ellipse(x_coordinate[i], 250, 15 * i, 15 * i)
        fill(0)
        ellipse(x_coordinate[i], 250, 3, 3)

def keyPressed():
    if key == "s": saveFrame("myProcessing.png")
