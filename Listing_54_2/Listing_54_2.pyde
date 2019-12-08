class FunnyRect(): 

    def setCenter(self, x,y):
        self.cx = x
        self.cy = y

    def setSize(self, a):
        self.a = a

    def render(self):
        rect(self.cx, self.cy, self.a, self.a)
        
    def colors(self,b):
        fill(b)

funnyRect = FunnyRect()
funnyRect1 = FunnyRect()
counter = 0

def setup():
    size(600,600)
    smooth()
    noStroke()
    rectMode(CENTER)
    funnyRect.setSize(50)
    funnyRect1.setSize(50)

def draw():
    global counter
    background(255)
    
    objX = mouseX +sin(counter)*150
    objY = mouseY +cos(counter)*150
    
    funnyRect.colors(50)
    funnyRect.setCenter(mouseX, mouseY)
    funnyRect.render()
    
    funnyRect1.colors(180)
    funnyRect1.setCenter(objX, objY)
    funnyRect1.render()
    
    counter +=0.05
    
def mouseClicked():
    currentSize = funnyRect.a
    currentSize += 50
    funnyRect1.setSize(currentSize)
