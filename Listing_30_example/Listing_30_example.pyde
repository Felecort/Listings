def setup():
    background(255)
    size(500, 500)
    smooth()

l1x1 = l1y1 = 0
l1x2 =  l1y2 = 500
flug = 1
mr = 10
mg = 150
mb = 100

def draw():
    global mr, mg, mb, l1x1, l1y1, l1x2, l1y2, flug
    background(0)
    strokeWeight(120)
    stroke(mr, mg, mb, 25)
    line(l1x1, l1y1, l1x2, l1y2)
    i = 0
    while i < 11:
        k = i*50
        stroke(mr, mg, mb, (255/11)*i)
        line(l1x1 + k, l1y1, l1x2, l1y2 - k)
        line(l1x1, l1y1 + k, l1x2 - k, l1y2)

        if l1x1 == l1x2 or l1x1 + k == l1x2 or l1x1 == l1x2 - k:
            mr = random(0,150)
            mg = random(0,150)
            mb = random(0,150)
        i += 1
    
    
    l1x1 = l1x1 + flug
    l1y1 = l1y1 + flug
    l1x2 = l1x2 - flug
    l1y2 = l1y2 - flug
    if l1y2 < 0 or l1y2 > 500:
        flug = flug*(-1)
