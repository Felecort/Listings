
a = [[10, 0] for i in range(10)]
step = 30

def setup():
    size(500, 500)
    smooth()
    noStroke()
    myInit()

def myInit():
    for i in range(len(a)): 
        a[i] = [random(0, 10)]
        for j in range(len(a[i])):  
            a[i][j] = random(0, 30)

def draw():
    global step
    fill(180, 50)
    background(10)
    for i in range(len(a)):
        for j in range(len(a[i])): 
            stroke(100)
            strokeWeight(1)
            fill(50)
            rect(i*step + 100, j*step + 100, step , step)
            
            noStroke()
            fill(250, 90)
            ellipse(i*step+115, j*step+115, a[i][j], a[i][j])

def mouseClicked():
    myInit()
