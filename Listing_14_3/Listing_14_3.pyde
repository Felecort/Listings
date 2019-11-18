def setup():
  size(500, 500)
  smooth()
  background(255)
  strokeWeight(30)
  noLoop()

def draw():
  for i in range (7):
    stroke(20)
    line(50 + 50 * i, 200, 150 + 50 * i, 300)
