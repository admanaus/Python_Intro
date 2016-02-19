# futval_graph.py

from graphics import *

def main():
    # Introduction
    print ("This program plots the growth of a ten year investment.")

    # Get principal and interist rate
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annualized interist rate, for example, 0.15: "))

    #Create a praphics window with labels on the left side
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    Lv1 = 230  # lv1 = label variable one
    Lv2 = 0.0  # lv2 = label variable two
    for i in range (5):
        Text(Point(20, Lv1), round(Lv2,1)).draw(win)
        Lv1 = Lv1 - 50
        Lv2 = Lv2 + 2.5

    # Draw a bar for the inital principal
    height = principal * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230-height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # Draw bars for sucsessive years
    for year in range (1, 11):
        # calculate value for the next year
        principal = principal * (1 + apr)
        # draw bar for this value
        xll = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(xll, 230), Point(xll+25, 230-height))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    input("Press <Enter> to quit")
    win.close()

main()
