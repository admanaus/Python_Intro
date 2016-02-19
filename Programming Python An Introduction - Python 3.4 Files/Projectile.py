# projectile.py

"""projectile.py
Provides a simple class for modeling the flight of projectiles."""

from math import pi, cos, sin, radians

class Projectile:

    """Simulates the flight of a simple projectiles near the earth's surface,
ignoring wind resistance.  Tracking is done in two dimensions,
height (y), and distance (x)."""
    
    def __init__(self, angle, velocity, height):
        """Creates a projectile with a given launch angle, initial
    velocity and height"""
        self.xpos = 0.0
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)
        
    def update(self, time):
        """Update the state of the ppojectile to move it time
    seconds in it's flight"""
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - 9.8 * time
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
        self.yvel = yvel1

    def getX(self):
        """Returns the y position (height) of this projectile"""
        return self.xpos

    def gety(self):
        """Returns the x position (distance) of this projectile"""
        return self.ypos



    
        
