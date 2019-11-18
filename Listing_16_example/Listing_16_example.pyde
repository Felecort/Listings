def setup():
  size(500, 500)
  smooth()
  background(255)
  strokeWeight(30)
  noLoop()

def draw():
  stroke(20)
  i = 1
  line(i*50, 200, 150 + (i-1)*50, 300)
  i = 2
  line(i*50, 200, 150 + (i-1)*50, 300)
  i = 3
  line(i*50, 200, 150 + (i-1)*50, 300)
