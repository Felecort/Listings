def setup():
  size(500, 500)
  smooth()
  background(255)
  strokeWeight(30)
  noLoop()

def draw():
  stroke(20)
  line(1*50, 200, 150 + (1-1)*50, 300)
  line(2*50, 200, 150 + (2-1)*50, 300)
  line(3*50, 200, 150 + (3-1)*50, 300)
