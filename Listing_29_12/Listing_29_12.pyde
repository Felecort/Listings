def setup():
    background(255)
    size(500, 500)
    smooth()

l1x1 = l1y1= 0
l1x2 = l1y2 = 500
flug = 1

def draw():
    global l1x1, l1y1, l1x2, l1y2, flug
    background(60)
    strokeWeight(50)
    line(l1x1, l1y1, l1x2, l1y2)

    for i in range(20):
        k = i * 50
        if l1y2 < 255:
            stroke(120, 0, 120, 20 + i * 10)
        else:
            stroke(124, 252, 0, 20 + i * 10)
        line(l1x1 + k, l1y1, l1x2, l1y2 - k)
        line(l1x1, l1y1 + k, l1x2 - k, l1y2)
    
    l1x1 = l1x1 + flug
    l1y1 = l1y1 + flug
    l1x2 = l1x2 - flug
    l1y2 = l1y2 - flug
    if l1y2 < 0 or l1y2 > 500:
        flug = flug * ( -1)
