
radius = 50
centerX = centerY = 250
length = 350
angle = PI/4
weight = 1
counter  = G = B = 0
R = 255
class MyLine():
    
    def render(self, centerX, centerY, angle, R, G, B):
        x1 = centerX - cos(angle)*length/2
        y1 = centerY + sin(angle)*length/2
        x2 = centerX + cos(angle)*length/2
        y2 = centerY - sin(angle)*length/2
                
        stroke(50,100)
        strokeWeight(weight)
        line(x1,y1,x2,y2)
        fill(R, G, B, 100)
        strokeWeight(2)
        stroke(B, R, G)
        ellipse(x2, y2, 12, 12)
        ellipse(x1, y1, 12, 12)

my_line = MyLine()

def setup():
    size(500,500)
    smooth()
    background(0)
    
    
def draw():
    global counter, radius, R, G, B
    counter += 0.05
    
    if (counter > 2*PI):
        counter = 0
        radius += 50
    if R == 255 and G == 0:
        B += 5
    if G == 0 and B == 255:
        R -= 5
    if R == 0 and B == 255:
        G += 5
    if R == 0 and G == 255:
        B -= 5
    if G == 255 and B == 0:
        R += 5
    if R == 255 and B == 0:
        G -= 5
    my_line.render(width/2 + sin(counter)*radius, height/2 + cos(counter)*radius, counter*2, R, G, B)
