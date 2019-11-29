
def setup():
    size(1000, 1000)
    smooth()
    background(0)
    strokeWeight(50)

counter = counter1 = nx = ny = 0
cx = cy = 500
cRadius = 10
switcher = 1

def draw():
    global counter , counter1 , nx , ny, cRadius, switcher
    if switcher > 0: 
        nx = cos(counter1)*cRadius + cx
        ny = sin(counter1)*cRadius + cy
        stroke(0, 50)
    else:
        nx = sin(counter1)*cRadius + cx
        ny = cos(counter1)*cRadius + cy
        stroke(250, 50)
    
    switcher *= -1

    x1 = nx - sin(counter)*(20)
    y1 = ny - cos(counter)*(20)
    x2 = nx + sin(counter)*(20)
    y2 = ny + cos(counter)*(20)

    line(x1, y1, x2, y2)

    counter += 0.1
    if counter > 2*PI: 
        counter = 0
    
    counter1 += 0.01
    cRadius += counter / 50

    if counter1 > 2*PI: 
        counter1 = 0
