num = 60
mx = [1]*60
my = [1]*60

def setup():
    size(640,360)
    noStroke()
    fill(255,153)
    
def draw():
    background(51)
    which = frameCount % num
    mx[which] = mouseX
    my[which] = mouseY
    
    for i in range(0, num):
        index = (which +1 +i) % num
        ellipse(mx[index], my[index], i, i)
