
def setup():
  global img1, img2
  background(100)
  smooth()
  img1 = loadImage("vp.jpg")
  img2 = loadImage("ob.jpg")

  size(275, 168)

def draw():
  myTintBO = map(mouseX, 0, width, 0, 255)
  myTintVP = map(mouseX, 0, width, 255, 0)

  tint(255, myTintVP)
  image(img1, 0, 0)
  tint(255, myTintBO)
  image(img2, 0, 0)
