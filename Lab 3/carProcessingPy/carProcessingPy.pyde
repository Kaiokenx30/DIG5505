# Even though there are multiple objects, we still only need one class. 
# No matter how many cookies we make, only one cookie cutter is needed.
class Pyramid(object):
    
    def __init__(self, c):
        self.c = c
    
    def spawn(self):
        if ((keyPressed) and (key == 'w')):
            stroke(0)
            fill(self.c)
            rectMode(CENTER)
            triangle(30, 75, 58, 20, 86, 75)

class Oil(object):
    
    def __init__(self, c):
        self.c = c
        
    def oilshape(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(mouseX, mouseY, 20, 20)
        
    def mousePressed(self):
        myOil1.oilshape();

class Rock(object):
    
    def __init__(self, c):
        self.c = c
        
    def rockshape(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(random(100), random(100), 10, 10);
        
        
class Car(object):
# The Constructor is defined with arguments.
    def __init__(self, c, xpos, ypos, xspeed):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        
    def display(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, 20, 10);
        
    
    def drive(self):
        self.xpos = self.xpos + self.xspeed;
        if self.xpos > width:
            self.xpos = 0
        myCar1.form();
    
    def form(self):
        if ((keyPressed) and (key == ' ')):
            rect(self.xpos, self.ypos, 40, 10);
        else: 
            rect(self.xpos, self.ypos, 20, 10);
    
myCar1 = Car(color(255, 0, 0), 0, 100, 2)
myCar2 = Car(color(0, 255, 255), 0, 10, 1)

myRock1 = Rock(color(100, 100, 100))

myOil1 = Oil(color(0, 0, 0))

myPyr = Pyramid(color(100,125,150))
    
def setup():
    size(200,200)

def draw(): 
  background(255)
  myRock1.rockshape()
  myCar1.drive()
  myCar1.display()
  myCar2.drive()
  myCar2.display()
  myOil1.mousePressed()
  fill(30)
  textSize(15)
  text("Press W", 100, 150)
  myPyr.spawn()
