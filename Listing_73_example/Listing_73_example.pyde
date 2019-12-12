
def setup():
    global img
    background(100)
    smooth()
    size(1000,1000)
    img = loadImage("000.jpg")

def draw():
    global img
    background(100)
    image(img, mouseX, mouseY)
