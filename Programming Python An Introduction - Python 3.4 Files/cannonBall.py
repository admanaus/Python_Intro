# cannonBall.py
#   This program simulates the flight of a cannon ball.

from math import pi, cos, sin, radians

def main():
    angle = eval(input('Enter the launch angle (in degrees):'))
    vel = eval(input('Enter th einitial velocity (in meters / second):'))
    h0 = eval(input('Enter the initial height (in meters):'))
    time = eval(input(
        'Enter the time interval between position calculations: '))
    
    # convert degrees to radians 
    theta = radians(angle)

    # set the initial position and velocities in x and y directions
    xpos = 0.0
    ypos = h0
    xvel = vel * cos(theta)
    yvel = vel * sin(theta)

    # loop until the ball hits the ground
    while ypos >= 0.0:
        xpos = xpos + time * xvel
        yvel1 = yvel - time * 9.8
        ypos = ypos + time * (yvel + yvel1) / 2.0
        yvel = yvel1

    print("\nDistance traveled: {0:0.1f} meters.".format(xpos))

if __name__ == '__main__': main()       
    
