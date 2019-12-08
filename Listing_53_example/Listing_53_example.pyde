
cx = cy = fsize = counter = 0

class FunnyRect():

  def setCenter(self, x, y):
    self.cx = x
    self.cy = y
  
  def setSize(self, size):
    self.fsize = size
  
  def render(self):
    rect(self.cx, self.cy, self.fsize , self.fsize)

funny_rect = FunnyRect()
funny_rect1 = FunnyRect()

def setup():
  size(600, 600)
  smooth()
  noStroke()
  rectMode(CENTER)
  funny_rect.setSize(50)
  funny_rect1.setSize(20)

def draw():
  global counter
  background(255)
  fill(50)
  objX = mouseX + sin(counter)*150
  objY = mouseY + cos(counter)*150
  funny_rect.setCenter(mouseX , mouseY)
  funny_rect.render()
  funny_rect1.setCenter(objX , objY)
  funny_rect1.render()
  counter += 0.05
