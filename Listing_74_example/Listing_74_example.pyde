
def setup():
  global img0, img1, img2, img3
  background(100)
  smooth()
  img0 = loadImage("i000.png")
  img1 = loadImage("i001.png")
  img2 = loadImage("i002.jpg")
  img3 = loadImage("i003.jpg")
  size(1000, 563)

def draw():
  background(100)
  image(img0, 0, 0)
  image(img1, mouseX * 0.7 - 150, 100)
  image(img2, 0, 0)
  image(img3, width - mouseX * 1.5, 35)
