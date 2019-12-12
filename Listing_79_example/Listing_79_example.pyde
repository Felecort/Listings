
lg_diam = lg_rad = lg_circ = sm_diam = cx = cy = 0

def setup():
    global lg_diam, lg_rad, lg_circ, sm_diam, cx, cy
    background(100)
    smooth()
    size(500, 400)
    noStroke()

    lg_diam = width * .55
    lg_rad = lg_diam / 2
    lg_circ = PI * lg_diam

    cx = width / 2
    cy = height / 2

    colorMode(HSB)

def draw():
    fill(0,10)
    rect(0,0,width ,height)

    nbr_circles = map(mouseX , 0, width , 6, 50)
    sm_diam = (lg_circ / nbr_circles)

    myColor = map(mouseY , 0, height , 150, 255)

    filter(BLUR , 3)

    fill(myColor ,180,190,100)

    for i in range(int(nbr_circles)):
        angle = i * TWO_PI / nbr_circles

        x = cx + cos(angle) * lg_rad
        y = cy + sin(angle) * lg_rad

        ellipse(x, y, sm_diam , sm_diam)

def keyPressed():
    if key == "s": saveFrame("myProcessing" + frameCount + ".jpg ")
