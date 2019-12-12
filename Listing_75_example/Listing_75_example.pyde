
isAnimate = True 
currentFrame = 1

def setup():
  global img1, img2, img3
  background(100)
  smooth()
  size(800, 800)
  frameRate(12)
  img1 = loadImage("000.png")
  img2 = loadImage("001.png")
  img3 = loadImage("002.png")

def draw():
  global isAnimate, currentFrame
  background(100)

  if isAnimate:
    if currentFrame == 1:
      image(img1 , mouseX , mouseY)
    if currentFrame == 2:
      image(img2 , mouseX , mouseY)
    if currentFrame == 1:
      image(img3 , mouseX , mouseY)

  currentFrame += 0.5

  if currentFrame > 3:
    currentFrame = 1
  else: image(img1 , mouseX , mouseY)

def keyPressed(): 
  global isAnimate
  if isAnimate: isAnimate = False
  else: isAnimate = True 
