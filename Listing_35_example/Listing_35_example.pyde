def setup():
    size(500, 500)
    smooth()
    background(0)
    strokeWeight(1)

i = 0
k = 1
flug = 1
def upDate():
    global flug, i, k
    i = i + k
    if i == 255:
        k=-1

    if i == 0:
        k=1
    

def draw ():
    global flug
    stroke(i, 20)
    if flug == 1:
        line(mouseX , mouseY , random(0,500), 0)
    else: 
        line(mouseX , mouseY , random(0,500), random(0,500))

    upDate()

def keyPressed():
    global flug
    if key== "q":
        flug = flug*(-1)
    
    if key== "s":
        saveFrame("myProcessing.png")
