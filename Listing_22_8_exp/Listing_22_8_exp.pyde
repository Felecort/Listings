def setup():
  size(500, 500)
  smooth()
  background(255)
  noStroke()
  noLoop()

def draw():
  for j in range (10):
    for i in range(10):
      fill((i + j) / 2 * 20)
      rect(i * 40 + 50, j * 40 + 50, 35, 35)
