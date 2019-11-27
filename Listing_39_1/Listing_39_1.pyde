
def setup():
    size(500, 500)
    smooth()
    background(50)
    strokeWeight(2)
    noLoop()

cx = 250
cy = 250
cRadius = 200

def draw():
    i = 2*PI
    j = 0
    global cx, cy, cRadius
    while i > 0:
        stroke(j)
        x1 = cos(i+PI/2)*cRadius + cx
        y1 = sin(i+PI/2)*cRadius + cy
        line(250 , 250 , x1 , y1)
        
        line(cx , cy , cx , cy)
        i = i - 2*PI/255
        j += 1

def keyPressed():
    if key== "s": saveFrame(" myProcessing .png")
