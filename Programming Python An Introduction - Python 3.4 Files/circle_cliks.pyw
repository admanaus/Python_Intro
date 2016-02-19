# circle_cliks.pyw

# This program will draw a circle centered where the user clicks.

from graphics import *

def main():
    win = GraphWin()
    shape = Rectangle(Point(50,50), Point(100,100))
    shape.setFill("red")
    shape.setOutline("red")
    shape.draw(win)

    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        newShape = shape.clone()
        newShape.move(dx, dy)
        newShape.draw(win)

    win.close()
main()
