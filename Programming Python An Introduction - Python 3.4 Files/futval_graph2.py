# futval_graph.py

from graphics import *

def drawBar(window, year, height):
    # Draw a bar in the window for the given year w the given height
    bar = Rectangle(Point(year, 0), Point(year+1, height))
    bar.setFill('green')
    bar.setWidth(2)
    bar.draw(window)

def createLabelWindow():
    window = GraphWin("Investment Growth Chart", 640, 480)
    window.setBackground("white")
    window.setCoords(-1.75, -200 ,11.5, 10400)
    Lv1 = 0  # lv1 = label variable one
    Lv2 = 0.0  # lv2 = label variable two
    for i in range (5):
        Text(Point(-1, Lv1), round(Lv2,1)).draw(window)
        Lv1 = Lv1 + 2500
        Lv2 = Lv2 + 2.5
    return window

def main():
    print ("This program plots the growth of a 10-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annualized interist rate, for example, 0.15: "))

    win = createLabelWindow()
    drawBar(win, 0, principal)

    for year in range (1, 11):
        principal = principal * (1 + apr)
        drawBar(win, year, principal)

    input("Press <Enter> to quit")
    win.close()

main()
