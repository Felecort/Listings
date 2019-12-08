
fsize  = counter = angle = 0
centerX = centerY = 250
size1= 150
weight = 1

class MyEllipse():
    def MyEllipse():
        centerX = cX
        centerY = cY
        angle = cA
        size = eS
        weight = Ew

    def render(self, size1):
        fill(200, size1/20)
        x1 = centerX + cos(counter) * 100 - cos(angle) * size1 / 2
        y1 = centerY + sin(counter) * 100 + sin(angle) * size1 / 2

        stroke(250, 100)
        strokeWeight(weight)
        ellipse(x1,y1,size1,size1)
  
my_ellipse = MyEllipse()
 
def setup():
    size(500,500)
    smooth()
    background(10)
    my_ellipse = (250,250,0,150,1)

def draw():
    global counter
    counter += 0.01
    if counter > TWO_PI:
        counter = 0

    my_ellipse.render(sin(counter*4)*mouseX)
