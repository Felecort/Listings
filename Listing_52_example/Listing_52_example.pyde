
cx = cy = fsize = 0

class FunnyRect():

  def setCenter(self, x ,y):
    self.cx = x
    self.cy = y
  
  def setSize(self, size):
    self.fsize = size
  
  def render(self):
    rect(self.cx, self.cy, self.fsize , self.fsize)


FunnyRect = FunnyRect()

def setup():
  size(600, 600)
  smooth()
  noStroke()
  rectMode(CENTER)
  FunnyRect.setSize(50)


def draw():
  background(255)
  fill(50)
  FunnyRect.setCenter(mouseX , mouseY)
  FunnyRect.render()
