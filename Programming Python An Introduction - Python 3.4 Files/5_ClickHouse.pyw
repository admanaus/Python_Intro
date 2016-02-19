# 5_ClickHouse.pyw

from graphics import *

def main():

    #Create a window and prompt the user
    win = GraphWin('House', 800,800)
    win.setCoords(0.0, 0.0, 4.0, 4.0)
    guide = Text(Point(2, 0.25), 'Click to form the bottom left corner of the house.')
    guide.draw(win)

    #Get mouse clicks for the face of the house
    p1 = win.getMouse()
    guide.setText('Now click to form the top right corner of the house')
    p2 = win.getMouse()
    face = Rectangle(p1, p2)
    face.setFill('green')
    face.draw(win)
    
    #Find the width of the house to establish a door width
    doorWidth = (p2.getX() - p1.getX()) / 10

    #Get Mouse click for the door.
    guide.setText('Click to form the top of the door')
    p3 = win.getMouse()
    doorP1x = p3.getX() - doorWidth
    doorP1y = p1.getY()
    doorP2x = p3.getX() + doorWidth
    doorP2y = p3.getY()
    door = Rectangle((Point(doorP1x, doorP1y)),(Point(doorP2x, doorP2y)))
    door.setFill('purple')
    door.draw(win)
    
    #Establish the width of the window
    windowWidth = doorWidth / 2
    
    #Get mouse click for the window
    guide.setText('Now, click to form the center of the window')
    p4 = win.getMouse()
    windowP1x = p4.getX() - windowWidth
    windowP1y = p4.getY() - windowWidth
    windowP2x = p4.getX() + windowWidth
    windowP2y = p4.getY() + windowWidth                
    window = Rectangle(Point(windowP1x, windowP1y), Point(windowP2x, windowP2y))
    window.setFill('blue')
    window.draw(win)
    
    #Establist the top left corner of the roof
    topLeft = Point(p1.getX(), p2.getY())

    #Get mouse click for the roof
    guide.setText('Last, click to form the top of the roof')
    p5 = win.getMouse()
    roof = Polygon(topLeft, p5, p2)
    roof.setFill('red')
    roof.draw(win)
    
    #End the program
    guide.setText('Click to close')
    win.getMouse()
    win.close()

main()

    
    
