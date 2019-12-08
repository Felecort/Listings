class FunnyRect():
    
    def setCenter(self,x,y):
        self.cx = x
        self.cy = y

    def setSize(self,size): 
        self.size = size

    def render(self):
        rect(self.cx, self.cy, self.size, self.size)
        
    def colors(self,R, G, B):
        fill(R, G, B)

funnyRect = FunnyRect()
funnyRect1 = FunnyRect()
counter = 0
cx = 0
cy = 0
fsize = 0

def setup():
    size(600,600)
    smooth()
    noStroke()
    rectMode(CENTER)
    funnyRect.setSize(50)
    funnyRect1.setSize(50)

def draw():
    background(255)
    global counter
    
    objX = mouseX +sin(counter)*150
    objY = mouseY +cos(counter)*150
    
    funnyRect.colors(255, 0, 0)
    funnyRect.setCenter(mouseX, mouseY)
    funnyRect.render()
    
    funnyRect1.colors(0, 0, 255)
    funnyRect1.setCenter(objX, objY)
    funnyRect1.render()
    
    counter +=0.05
