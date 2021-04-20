from graphics import *

#graphical window
win = GraphWin("FasterGame", 600, 500)
win.setBackground("RoyalBlue")

#Page with title of the game
def intro():

    t = Text(Point(300, 300), "Click again to quit!")
    t.setFace("arial")
    t.setSize(15)
    t.setStyle("bold")
    t.draw(win)
    win.getMouse()

#Intructions for the user after first click
def instructions():

    t = Text(Point(300, 300), '''
    In this game your fastest self WILL be revield. Your mission
    is to select as quickly as possible the correct colored square
    wich will be spesified in the superior part of the window. You
    can time your self and challenge your reflexes.

    press anywhere to start the game. GOOD LUCK! 
    ''')
    t.setFace("arial")
    t.setSize(12)
    t.setStyle("bold")
    t.draw(win)
    win.getMouse()



def squares(x1, y1, x2, y2, color):

    r = Rectangle(Point(x1 , y1), Point(x2 , y2)) 
    r.setFill(color) 
    r.setWidth(1)
    r.draw(win)    
  
    
def main():

    intro()   
    instructions()  
    
    win.setBackground("gray")

    squares(4, 4, 104, 104, "light salmon")
    squares(114, 4, 214, 104, "blue")
    squares(224, 4, 324, 104, "red")
    squares(334, 4, 434, 104, "yellow")
    squares(444, 4, 544, 104, "purple")
    squares(4, 4, 104, 104, "orange")
       

    win.getMouse()
    win.close()

main()
