def setup():
    size(300, 300)
    smooth()
    strokeWeight(30)
    background(0)

def draw():
    stroke(frameCount)
    line(100 + frameCount, frameCount, frameCount, frameCount + 100 )
    line(frameCount + 25, frameCount + 25, frameCount + 25, frameCount + 25)
