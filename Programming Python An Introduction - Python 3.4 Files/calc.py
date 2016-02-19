# calc.py
#   Illistrates use of objects and lists to build a simple GUI

from graphics import *
from button import Button

class Calculator:
    
    def __init__(self):
        # This class impliments a simple calculator GUI
        win = GraphWin('Calculator', 600, 600) 
        win.setCoords(0,0,6,7) # Divides the window into a 6 x 7 grid to simplify button placement
        win.setBackground('slategray')
        self.win = win
        # Now create the widgits
        self.__createButtons()
        self.__createDisplay()

    def __createButtons(self):
        # create list of buttons
        # start with all the standard sized buttons
        # bSpecs gives center coords and label of buttons
        bSpecs = [(2,1,'0'), (3,1,'.'),
                  (1,2,'1'), (2,2,'2'), (3,2,'3'), (4,2,'+'), (5,2,'-'),
                  (1,3,'4'), (2,3,'5'), (3,3,'6'), (4,3,'*'), (5,3,'/'),
                  (1,4,'7'), (2,4,'8'), (3,4,'9'), (4,4,'<-'),(5,4,'C')]
        self.buttons = []
        for (cx, cy, label) in bSpecs:
            self.buttons.append(Button(self.win, Point(cx,cy), .75, .75, label))
        # create the large = button
        self.buttons.append(Button(self.win, Point(4.5, 1), 1.75, .75, '='))
        # activate all buttons
        for b in self.buttons:
            b.activate()

    def __createDisplay(self):
        bg = Rectangle(Point(.5, 5.5), Point(5.5, 6.5))
        bg.setFill('white')
        bg.draw(self.win)
        text = Text(Point(3, 6), "")
        text.draw(self.win)
        text.setFace('courier')
        text.setStyle('bold')
        text.setSize(20)
        self.display = text

    def getButton(self):
        # Waits fr a button to be clicked and returns the label of
        #   the button that was clicked.
        while True:
            p = self.win.getMouse()
            for b in self.buttons:
                if b.clicked(p):
                    return b.getLabel() # method exit

    def processButton(self, key):
        # Updates the display of the calculator for press of this key
        text = self.display.getText()
        if key == 'C':
            self.display.setText("")
        elif key == '<-':
            # Backspace, slice off the last character
            self.display.setText(text[:-1])
        elif key == '=':
            # Evaluate the expression and display the result
            # the try...except mechanism "catches" errors in the
            # formula being evaluated.
            try:
                result = eval(text)
            except:
                result = 'Error'
            self.display.setText(str(result))
        else:
            # Normal key press, append it to the end of the display
            self.display.setText(text + key)

    def run(self):
        # Infinite 'event loop' to process button clicks.
        while True:
            key = self.getButton()
            self.processButton(key)

# Ths runs the program.
if __name__ == '__main__':
    # First create the calculator object
    theCalc = Calculator()
    # Now call the calculator's run method.
    theCalc.run()
    
    
    
        
