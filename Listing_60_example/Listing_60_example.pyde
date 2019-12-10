
x_coordinate = [x_coordinate for x_coordinate in range(10)]

def setup():
 size(500, 500)
 smooth()
 noStroke()
 for i in range(0, len(x_coordinate)):
    x_coordinate[i] = 35*i + 90

def draw():
 background(50)

 for coordinate in (x_coordinate):
    fill(200)
    ellipse(coordinate , 250, 30, 30)
    fill(0)
    ellipse(coordinate , 250, 3, 3)

def keyPressed():
    if key == "s":
        saveFrame("myProcessing.png")
