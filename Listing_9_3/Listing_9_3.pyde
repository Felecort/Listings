k = 0

def setup():
  size(600, 600)
  noLoop()

def drawMyScene(myColor):
  global k 
  rotate(PI/4 * k)
  fill(myColor)
  rect(0,50, 150, 50)
  rect(50,0, 50, 150)
  k += 1

def draw():
  background(20)
  smooth()
  noStroke()

  pushMatrix()
  translate(100, 20)
  drawMyScene(180)
  popMatrix()
  
  pushMatrix()
  translate(220, 110)
  scale(2)
  drawMyScene(220)
  popMatrix()
  
  pushMatrix()
  translate(520, 390)
  scale(1.4)
  drawMyScene(80)
  popMatrix()
