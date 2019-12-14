





angle = 0
snakesize = 5
time = 0
headx = [[i] for i in range(2500)]
heady = [[i] for i in range(2500)]

applex = (round(random(60))+1)*8
appley = (round(random(60))+1)*8
redo = True
stopgame = False

def setup():
    global img_win, img_lose
    img_win = loadImage("win.jpg")
    img_lose = loadImage("lose.jpg")
    restart()
    size(500, 500)
    textAlign(CENTER)

def draw():
    global applex, appley, stopgame, time
    if stopgame:
        pass
    else:
        time += 1
        fill(255,0,0)
        stroke(0)
        rect(applex,appley,8,8)
        fill(0)
        stroke(0)
        rect(0,0,width,8)
        rect(0,height-8,width,8)
        rect(0,0,8,height)
        rect(width-8,0,8,height)
    if time % 5 == 0:
        travel()
        display()
        checkdead()

def keyPressed():
    global heady, headx, angle
    if key == CODED:
        if keyCode == UP and angle!=270 and (heady[1]-8)!=heady[2]:
            angle=90
        if keyCode == DOWN and angle!=90 and (heady[1]+8)!=heady[2]:
            angle=270
        if keyCode == LEFT and angle!=0 and (headx[1]-8)!=headx[2]:
            angle=180
        if keyCode == RIGHT and angle!=180 and (headx[1]+8)!=headx[2]:
            angle=0
        if keyCode == SHIFT:
            restart()

def travel():
    global angle, headx, heady, snakesize
    for i in range(snakesize, 0, -1):
        if i != 1:
            headx[i] = headx[i-1]
            heady[i] = heady[i-1]
        else:
            if angle == 0:
                headx[1]+= 8
            if angle == 90:
                heady[1]-= 8
            if angle == 180:
                headx[1]-= 8
            if angle == 270:
                heady[1]+= 8

def display():
    global  headx, heady, snakesize, applex, appley
    if headx[1] == applex and heady[1] == appley:
        snakesize += 1
        redo = True

        while redo:
            applex = (round(random(47)) + 1) * 8
            appley = (round(random(47)) + 1) * 8
            for i in range(1, snakesize):
                if applex == headx[i] and appley == heady[i]:
                    redo = True
                else:
                    redo = False
                    i = 1000
    stroke(255,255,255)
    fill(0)
    rect(headx[1],heady[1],8,8)
    fill(255)
    rect(headx[snakesize],heady[snakesize],8,8)

def checkdead():
    global snakesize, headx, heady, stopgame, img_win, img_lose
    if snakesize == 30:
        image(img_win, 0, 0)
        fill(0)
        text("YOU WIN!",250,330)
        text("Score:  " + str(snakesize - 5) + " apples eaten", 250,  355)
        text("Press SHIFT to RESTART", 250, 380)
        stopgame = True
    for i in range(2, snakesize+1):
        if headx[1] == headx[i] and heady[1] == heady[i]:
            image(img_lose, 0, 0)
            fill(255)
            text("YOU LOSE!", 250,330)
            text("Score:  " + str(snakesize - 5) + " apples eaten", 250,  355)
            text("Press SHIFT to RESTART", 250, 380)
            stopgame = True

        if headx[1] >= width - 8 or heady[1] >= height - 8 or headx[1] <= 0 or heady[1] <= 0:
            image(img_lose, 0, 0)
            fill(255)
            text("YOU LOSE!", 250, 330)
            text("Score:  "+str(snakesize - 5)+" apples eaten", 250, 355);
            text("Press SHIFT to RESTART", 250, 380)
            stopgame = True


def restart():
    global headx, heady, stopgame, appley, applex, time, redo, angle, snakesize
    background(255)
    headx[1] = 200
    heady[1] = 200
    for i in range(2, 1000):
        headx[i] = 0
        heady[i] = 0
    stopgame = False
    applex = (round(random(60)) + 1) * 8
    appley = (round(random(60)) + 1) * 8
    snakesize = 5
    time = 0
    angle = 0
    redo = True
