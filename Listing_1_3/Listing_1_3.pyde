def setup():
    size(300,300)
    background(255)  # Градиентный переход от черного "0" до белого "255"
    smooth()
    noLoop()
    
def draw():
    strokeWeight(30)
    stroke(100)
    line(100, 100, 200, 200)
    line(200, 100, 100, 200)
