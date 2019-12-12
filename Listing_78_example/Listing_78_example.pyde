
def setup():
    global img0, img1
    background(100)
    smooth()
    noStroke()
    img0 = loadImage("sw.png")
    img1 = loadImage("swbb.png")
    size(1920, 1080)

def draw():
    if frameCount == 1: image(img1, 0, 0)

    pointSize = map(mouseX , 0, width , 0, 100)
    pointAlpha = map(mouseY , 0, height , 0, 255)

    x = random(img0.width)
    y = random(img0.height)

    loc = int(x + y * img0.width)
    img0.loadPixels()

    r = red(img0.pixels[loc])
    g = green(img0.pixels[loc])
    b = blue(img0.pixels[loc])

    fill(r, g, b, pointAlpha)
    ellipse(x, y, pointSize, pointSize)
    tint(255, 2)
    image(img1, 0, 0)

def keyPressed():
    saveFrame("myProcessing" + frameCount + ".jpg ")
