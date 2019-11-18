def setup():
  size(500, 500)
  smooth()
  background(255)
  noStroke()
  noLoop()

def draw():
  for i in range(10):
    fill(i*20)
    rect(i*40+50, 220, 35, 35)
