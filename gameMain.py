from graphics import *

#graphical window
win = GraphWin("FasterGame", 600, 500)
win.setBackground("RoyalBlue")

#title and introduction of the game
def intro():

    t = Text(Point(300, 200), "FasterGame!")
    t.setFace("arial")
    t.setSize(20)
    t.setStyle("bold")
    t.draw(win)
    win.getMouse()
    t.setText('''
    In this game your fastest self WILL be revield. Your mission
    is to select as quickly as possible the correct colored square
    which will be spesified in the superior part of the window. You
    can time your self and challenge your reflexes.

    Click anywhere two times to start the game. GOOD LUCK! 
    ''')
    t.setSize(13)
    win.getMouse()
    t.undraw() 



def squares(x1, y1, x2, y2, color):

    p1 = Point(x1 , y1)
    p2 = Point(x2 , y2)

    r = Rectangle(p1, p2) 
    r.setFill(color) 
    r.setWidth(1)
    r.draw(win)         

         
    
def main():

    intro()
    win.getMouse()

    win.setBackground("gray")

    squares(4, 4, 104, 104, "light salmon")    
    squares(114, 4, 214, 104, "blue")
    squares(224, 4, 324, 104, "red")
    squares(334, 4, 434, 104, "yellow")
    squares(444, 4, 544, 104, "purple")

    p = win.getMouse()  
    r = Rectangle(Point(p < 124 and p < 224, p > 4 and p < 104), Point(p < 324 and p > 224, p < 4  and p < 104)) 
    
    if r:
        t = Text(Point(250,25),'CORRECTO')
        t.setStyle("bold")
        t.draw(win)
    else:
        t.setText('NO funciona esta mierda')
        t.draw(win)              

    win.getMouse()
    win.close()

main()
