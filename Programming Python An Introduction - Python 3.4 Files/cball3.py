# cball3.py

from math import pi, sin, cos, radians

class Projectile:
    
    from math import pi, sin, cos, radians
    
    def __init__(self, angle, velocity, height):
        self.xpos = 0.0
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)
        
    def update(self, time):
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - 9.8 * time
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
        self.yvel = yvel1

    def getX(self):
        return self.xpos

    def gety(self):
        return self.ypos

def getInputs():
    a = 45
    v = 100
    h = 10
    t = 1
    
##    a = eval(input("Enter the launch angle (in degrees): "))
##    v = eval(input("Enter the initial velocity (in meters / second): "))
##    h = eval(input("Enter the initial height (in meters): "))
##    t = eval(input("Enter the time interval between position calculations: "))
    return a, v, h, t

def main():
    angle, vel, h0, time = getInputs()
    cball = Projectile(angle, vel, h0)
    while cball.gety() >= 0:
        cball.update(time)
    print("\nDistance traveled: {0:0.1f} meters.".format(cball.xpos))



if __name__ == '__main__': main()
    
        

