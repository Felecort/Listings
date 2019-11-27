windowWidth = 500
windowHeight = 500
ellipseSize = 100
ellipseWidth = 200
ellipseHeight = 300

def setup():
  size(windowWidth, windowHeight)
  smooth()
  background(255)
  fill(50, 80)
  stroke(100)
  strokeWeight(3)
  noLoop()
  
def draw():
  ellipse(windowWidth/2, windowHeight/2 - ellipseSize/2, ellipseWidth, ellipseHeight)
  ellipse(windowWidth/2 - ellipseSize/2, windowHeight/2, ellipseWidth, ellipseHeight)
  ellipse(windowWidth/2 + ellipseSize/2, windowHeight/2, ellipseWidth, ellipseHeight)
  ellipse(windowWidth/2, windowHeight/2 + ellipseSize/2, ellipseWidth, ellipseHeight)
