
def setup():
    global img1, img2
    background(100)
    smooth()
    img1 = loadImage("sw.png")
    img2 = loadImage("swbb.png")

    size(1920, 1080)
    strokeWeight(5)

def draw():
    if frameCount == 1:
        image(img2, 0,0)

    pointSize = map (mouseX, 0, width, 0, 100)
    pointAlpha = map(mouseY, 0, height, 0, 255)

    x = random(img1.width)
    y = random(img1.height)

    loc = int(x + y * img1.width)
    img1.loadPixels()

    r = red(img1.pixels[loc])
    g = green(img1.pixels[loc])
    b = blue(img1.pixels[loc])

    fill(r, g, b, pointAlpha)
    line(x, y, x+5, y+5)
    tint(255,2)
    image(img2, 0,0)

def keyPressed():
    saveFrame("myProcessing" + frameCount + ".jpg ")
