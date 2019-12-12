
isAnimate = True
currentFrame = 1

def setup():
    global img1, img2, img3
    smooth()
    size(500, 500)
    frameRate(12)
    img1 = loadImage("000.png")
    img2 = loadImage("001.png")
    img3 = loadImage("002.png")

def draw():
    global currentFrame, isAnimate

    if (pmouseX - mouseX) > 0:
        if isAnimate:
            if currentFrame == 1:
                background(100)
                image(img1, mouseX, mouseY)
            if currentFrame == 2:
                background(100)
                image(img2, mouseX, mouseY)
            if currentFrame == 3:
                background(100)
                image(img3, mouseX, mouseY)
            currentFrame += 1
            if currentFrame > 3:
                currentFrame = 1
        else:
            background(100)
            image(img3, mouseX, mouseY)
    if (pmouseX - mouseX) < 0:
        if isAnimate:
            if currentFrame == 1:
                background(100)
                image(img3, mouseX, mouseY)
            if currentFrame == 2:
                background(100)
                image(img2, mouseX, mouseY)
            if currentFrame == 3:
                background(100)
                image(img1, mouseX, mouseY)
            currentFrame += 1
            if currentFrame > 3:
                currentFrame = 1
        else:
            background(100)
            image(img3, mouseX, mouseY)
    else:
        pass

def keyPressed():
    global isAnimate
    if isAnimate: isAnimate = False
    else: isAnimate = True
