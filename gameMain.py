from graphics import *

win = GraphWin("FasterGame", 550, 500)
win.setBackground("RoyalBlue")

def intro():

    t = Text(Point(275, 200), "FasterGame!")
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
    r.setOutline("white")
    r.draw(win)



def puzzle_1():

    win.setBackground("black")

    #Fake maze list:
    list_1 = [squares(0, 0, 25, 400, "white"),    
    squares(0, 375, 400, 400, "white"),
    squares(0, 0, 550, 20, "white"),
    squares(525, 0, 550, 400, "white"),
    squares(450, 375, 550, 400, "white"),
    squares(75, 0, 100, 100, "white"),
    squares(225, 75, 250, 300, "white"),
    squares(0, 150, 175, 175, "white"),
    squares(0, 225, 150, 250, "white"),
    squares(50, 275, 425, 300, "white"),
    squares(400, 275, 425, 350, "white"),
    squares(400, 325, 475, 350, "white"),
    squares(275, 150, 500, 175, "white"),
    squares(275, 150, 300, 225, "white"),
    squares(275, 225, 480, 250, "white"),
    squares(455, 250, 480, 350, "white"),
    squares(300, 75, 550, 100, "white"),
    squares(50, 300, 75, 350, "white"),
    squares(50, 325, 325, 350, "white"),
    squares(325, 325, 350, 375, "white"),
    squares(300, 75, 325, 125, "white"),
    ]    
    for x in range(len(list_1)): 
        list_1[x] 

    #Superior area circle:
    c = Circle(Point(275, 50), 10)
    c.setFill("red")
    c.setOutline("red")
    c.draw(win)
    t = Text(Point(350, 50), "<= You are here")
    t.setFace("arial")
    t.setSize(10)
    t.setStyle("bold")
    t.setTextColor("red")
    t.draw(win)

    t1 = Text(Point(345,450), "Your goal is here =>")
    t1.setTextColor("red")
    t1.setSize(10)
    t1.draw(win)
    

    #Inferior area circle:
    p1 = Point(490,450)
    p2 = Point(510, 470)
    a = Rectangle(p1, p2)
    a.setFill("red") 
    a.draw(win)
    x1 = a.getP1().getX()
    y1 = a.getP1().getY()
    x2 = a.getP2().getX()
    y2 = a.getP2().getY()
    p = win.getMouse()   

    while x1 <= p.getX() <= x2 and y1 <= p.getY() <= y2:
        print('YESYESYES')
        p = win.getMouse()

    c_cor = c.getCenter()   
    
        l = Line(c_cor, p)
        l.setOutline("red")
        l.setArrow("first")
        l.draw(win)        
    
    #text(345, 450, 10, "Your goal is here =>", "red")

    

    win.getMouse()
    squares(0, 0, 550, 500, "gray")
    t2 = Text(Point(275,200), '''
        IF you clicked the inferior circle you are CORRECT.
        In the instructions we never mentioned that you had the task
        to actually solve the maze. Your mission was simply to get
        from your spawn point to the goal point (inferior red circle)
        with just one click.
        enter key one of the following keys:

        'a' to go back and do the maze puzzle again.
        'b' to continue with next puzzles.''')
    t2.setTextColor("red")
    t2.setSize(13)
    t2.draw(win)

    win.getMouse()
    
    
        
    



def main():

    intro()
    win.getMouse()    
    puzzle_1()
    
    

        
    #win.setBackground("gray")
                
               
    win.getMouse()
    win.close()

main()