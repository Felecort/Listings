
def setup():
    size(500, 500)
    smooth()

counter = 0
def draw():
    global counter
    noStroke()
    fill(10, 50)
    rect(-1,-1,width/2,height +1)

    ny = sin(counter)*100+200
    nx = counter *10

    stroke(250)
    strokeWeight(20)
    line(nx , ny , nx , ny)

    counter = counter + 0.1
    if nx > width:
        counter = 0


def keyPressed():
    if key== "s":
        saveFrame(" myProcessing .png")
