
click = 0

def setup():
    global img1, img2
    background(100)
    smooth()
    img1 = loadImage("ob.jpg")
    img2 = loadImage("vp.jpg")
    size(275, 168)
    
def mouseClicked():
    global click
    if mouseButton == RIGHT or mouseButton == LEFT:
        click -= 5
        if click > 100:
            click  = 100   

def draw():
    global click
    if click < 100:
        click += 0.1 
    myTint000 = map(click, 0, 100, 0, 255)
    myTint001 = map(click, 0, 100, 255, 0)
    tint(255, myTint001)
    image(img1, 0, 0)
    tint(255, myTint000)
    image(img2,0,0)
