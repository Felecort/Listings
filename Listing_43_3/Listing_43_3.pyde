
def setup():
    size(500, 500)
    smooth()
    background(0)
    strokeWeight(1)

counter = nx = ny = 0
cx = 250
cy = 250
def draw():
    global counter, nx, ny
    stroke(150, 1)
    for si in range(6):
        for ci in range(6): 
            nx = ci * 80 + 50
            ny = si * 80 + 50
            x1 = nx - sin(counter) * (100)
            y1 = ny - cos(counter) * (100)
            x2 = ny + sin(counter) * (100)
            y2 = nx + cos(counter) * (100)
            line(nx, ny, nx, ny)
            line(x1, y1, x2, y2)

    counter += 0.1
    if counter > 2*PI: 
        counter = 0
