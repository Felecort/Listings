centerX = centerY = length = angle = weight = 0
class MyLine():
  
  def render(self, centerX, centerY, angle):
    self.x1 = centerX - cos(angle)*length/2
    self.y1 = centerY + sin(angle)*length/2
    self.x2 = centerX + cos(angle)*length/2
    self.y2 = centerY - sin(angle)*length/2

    stroke(50, 100)
    strokeWeight(weight)
    line(self.x1, self.y1, self.x2, self.y2)
    strokeWeight(5)
    stroke(50)
    line(self.x2, self.y2, self.x2, self.y2)
    line(self.x1, self.y1, self.x1, self.y1)

myline = MyLine()

counter = 0
def setup():
  size(500, 500)
  smooth()
  background(255)
  myline = MyLine()
  myline.centerX = width/2
  myline.centerY = height/2
  myline.length = 350
  myline.angle = PI/4
  myline.weight = 1

def draw():
  global counter
  counter += 0.05
  if counter > TWO_PI: 
    counter = 0
  myline.render(width/2 + sin(counter)*50, width/2 + cos(counter)*50, counter*2)
