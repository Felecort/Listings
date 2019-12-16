#import datetime
#today = datetime.datetime.today()
#today = datetime.datetime.today()
#date = today.strftime("%Y-%m-%d_%H-%M")
#log_name = "log_" + date
#f = open(log_name + ".txt")


rotateCounter = 0

def setup():
  size(600, 600)
  smooth()
  background(0)

  font = loadFont("text.vlw")
  textFont(font, 48)

def draw():
  global rotateCounter
  translate(width/2, height /2)
  pushMatrix()
  rotate(rotateCounter)

  fill(255)
  text("Black", mouseX - width/2, mouseY - height /2)

  popMatrix()
  pushMatrix()
  rotate(-rotateCounter*1.5)

  fill(0)
  text(" White ", width/2 - mouseX , height/2 - mouseY)
  popMatrix()

  rotateCounter+=0.05
