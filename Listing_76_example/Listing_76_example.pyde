
def setup():
  global img0, img1
  size(1200, 595)
  background(100)
  smooth()
  colorMode(HSB)
  img0 = loadImage("0.jpg"); # 138 x 595
  img1 = loadImage("1.jpg")

def draw():
  background(100)
  for i in range(10):
    tint(i*25, 150, 255)
    if mouseX < i*120 + 120 and mouseX > i*120:
      noTint()
      image(img1, i*120, 0)
    else: image(img0, i*120, 0)
