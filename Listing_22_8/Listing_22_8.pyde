def setup():
    size(500, 500)
    smooth()
    background(255)
    noStroke()
    noLoop()

def draw():
    i = 0
    j = 0
    while j < 11:
        while i < 11:
            if j == 1 or j == 3 or j == 5 or j == 7 or j == 9:
                fill(220 - i * 20)
                rect(i * 40 + 30, 30 + 40 * j, 35, 35)
            else:
                fill(i * 20)
                rect(i * 40 + 30, 30 + 40 * j, 35, 35)
            i += 1
        j += 1
        i = 0
