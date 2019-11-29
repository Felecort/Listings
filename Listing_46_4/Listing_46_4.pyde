
def setup():
    size(500, 500)
    smooth()
    background(255)
    strokeWeight(1)

counter = counter1 = 0
cx = cy = 250
cRadius = 10

def draw():
    global counter, counter1, cx, cy, cRadius
    stroke(0, 50)

    nx = sin(counter1)*cRadius + cx
    ny = cos(counter1)*cRadius + cy

    x1 = nx - sin(counter)*(50)
    y1 = ny - cos(counter)*(50)
    x2 = nx + sin(counter)*(50)
    y2 = ny + cos(counter)*(50)
    
    stroke(random(0, 255),random(0, 255),random(0, 255), 50)
    fill(random(0, 255),random(0, 255),random(0, 255))
    ellipse(x1 , y1 , 20, 20)

    counter += 0.1
    if counter > 2*PI: 
        counter = 0

    counter1 += 0.01
    cRadius += counter1 /30

    if counter1 > 2*PI: 
        counter1 = 0

def keyPressed():
    if key == "s": saveFrame("myProcessing.png")
