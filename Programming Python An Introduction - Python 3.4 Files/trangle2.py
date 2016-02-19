# Program: trangle2.py
import math
from graphics import *

def square (x):
    return x * x

def distance(p1, p2):
	dist = math.sqrt(square(p2.getX() - p1.getX())
			 + square(p2.getY() - p1.getY()))
	return dist

def main():
    win = GraphWin('Draw a Triangle')
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), 'Click on three points')
    message.draw(win)

    # Get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # Use Polygone object to draw triangle
    triangle = Polygon(p1, p2, p3)
    triangle.setOutline('red')
    triangle.setFill('peachpuff')
    triangle.draw(win)

    # Calculate the perimiter of the triangle
    perim = distance(p1, p2) + distance(p2, p3) + distance(p3, p1)
    message.setText('Perimiter: {0:0.2f}'.format(perim))

    win.getMouse()
    win.close()

main()

