from graphics import *

#graphical window
win = GraphWin("FasterGame", 600, 500)
win.setBackground("gray")

def squares(x1, y1, x2, y2, color):

    r = Rectangle(Point(x1 , y1), Point(x2 , y2)) 
    r.setFill(color) 
    r.setWidth(1)
    r.draw(win)
    
    
    
def main():
    
    squares(4, 4, 104, 104, "light salmon")
    squares(114, 4, 214, 104, "blue")
    squares(224, 4, 324, 104, "red")
    squares(334, 4, 434, 104, "yellow")
    squares(444, 4, 544, 104, "purple")
    squares(4, 4, 104, 104, "orange")
    


    win.getMouse()
    win.close()

main()
'''
    #Dice 2
    r2 = Rectangle(Point(114 , 4), Point(214 , 104)) 
    r2.setFill("light salmon") 
    r2.setWidth(1)
    r2.draw(win)
    
    #Dice 3
    r3 = Rectangle(Point(224 , 4), Point(324 , 104)) 
    r3.setFill("light salmon") 
    r3.setWidth(1)
    r3.draw(win)
        
    #Dice 4
    r4 = Rectangle(Point(334 , 4), Point(434 , 104)) 
    r4.setFill("light salmon") 
    r4.setWidth(1)
    r4.draw(win)       
    
    #Dice 5
    r5 = Rectangle(Point(444 , 4), Point(544 , 104)) 
    r5.setFill("light salmon") 
    r5.setWidth(1)
    r5.draw(win)
'''
