centerX = centerY = 250
angle = size1 = weight = counter = 0

class MyEllipse():
    cX = centerX
    cY = centerY
    cA = angle
    eS = size1
    Ew = weight
        
    def render(self, size1):
        fill(200, size1/20)
        x1 = centerX - cos(angle) * size1 / 2
        y1 = centerY + sin(angle) * size1 / 2
        
        stroke(250, 100)
        strokeWeight(weight)
        ellipse(x1, y1, size1, size1)
        
my_ellipse = MyEllipse()
        
def setup():
    size(500,500)
    smooth()
    background(10)
    
def draw():
    global counter
    counter += 0.01
    if (counter > TWO_PI):
        counter = 0
        
    my_ellipse.render(sin(counter*4)*mouseX)
