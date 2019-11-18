def setup():
  size(500, 500)
  smooth()
  background(255)
  strokeWeight(30)
  noLoop()

def draw():
  stroke(20)
  line(50, 200, 150, 300)
  line(50 + 50, 200, 150 + 50, 300)
  line(50 + 50 + 50, 200, 150 + 50 + 50, 300)
