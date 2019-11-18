def setup():
  size(500, 500)
  smooth()
  background(255)
  strokeWeight(30)
  noLoop()
  stroke(0,50)

def draw():
  for i in range (0, 9):
    for k in range (0, 5):
      line(i*50, 100*k, 150 + (i-1)*50, 100 + 100*k)
      line(i*50 + 100, 100*k, 50 + (i-1)*50, 100 + 100*k)
