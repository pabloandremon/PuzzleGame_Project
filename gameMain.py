from graphics import *
import random

win = GraphWin("PuzzleGame", 550, 500)
win.setBackground("RoyalBlue")

def intro():

    t = Text(Point(275, 200), "PuzzleGame!")
    t.setFace("arial")
    t.setSize(20)
    t.setStyle("bold")
    t.draw(win)
    win.getMouse()
    t.setText('''
    In this game your will witness a series of puzzles. In the first
    puzzle, your mission is to go through a maze. With just one click
    get from you spawn point to the goal point.

    Click anywhere start the first puzzle game. GOOD LUCK! 
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

    t1 = Text(Point(350,450), "Your goal is here =>")
    t1.setTextColor("green")
    t1.setSize(10)
    t1.draw(win)
    

    #Inferior area circle:
    p1 = Point(415, 438)
    p2 = Point(450, 473)
    a = Rectangle(p1, p2)
    a.setFill("green") 
    a.draw(win)
    x1 = a.getP1().getX()
    y1 = a.getP1().getY()
    x2 = a.getP2().getX()
    y2 = a.getP2().getY()
    p = win.getMouse()   

    if x1 <= p.getX() <= x2 and y1 <= p.getY() <= y2:
        c_cor = c.getCenter()    
        l = Line(c_cor, p)
        l.setOutline("red")
        l.setArrow("first")
        l.draw(win)

        
        squares(0, 0, 275, 500, "green")
        t2 = Text(Point(130,200), '''
        GREAT JOB, you are correct!
        In the instructions we never
        mentioned that you had the task
        to actually solve the maze.
        Your mission was simply to get
        from your spawn point(red circle) 
        to the goal point (green square)
        with just one click.
        
        Click anywhere to go 
        to the next puzzle! ''')
        t2.setTextColor("black")
        t2.setSize(13)
        t2.draw(win)
        
     
    else:

        r = Rectangle(Point(150, 175), Point(440, 250)) 
        r.setFill("gray") 
        r.setWidth(1)
        r.setOutline("white")
        r.draw(win)

        t = Text(Point(275,200), '''
        WRONG!
        Click anywhere to try again''')
        t.setTextColor("red")
        t.setSize(13)
        t.draw(win)

        win.getMouse()
        t.undraw()
        r.undraw()
        puzzle_1()    
    
  
def puzzle_2():

    squares(0, 0, 550, 500, "gray")
    t = Text(Point(275,200), '''
    Welcome to puzzle #2, called:
    "Where are the squares?
    
    Click anywhere to get started."
     ''')
    t.setTextColor("black")
    t.setSize(13)
    t.draw(win)

    win.getMouse()
    t.undraw()

    squares(50, 20, 500, 100, "purple")
    t = Text(Point(275, 60), '''
    There are three mini houses: one is red, one is blue, one is white.
    If the red house is to the left of the house in the middle and 
    the blue house is to the right to the house in the middle.
    Where is The White House located? (select you best guess)
     ''')
    t.setTextColor("white")
    t.setSize(9)
    t.draw(win)

    squares(25, 200, 125, 300, "grey33")
    t = Text(Point(75, 250), 'Left')
    t.setTextColor("white")
    t.setSize(11)
    t.draw(win)

    squares(225, 200, 325, 300, "grey33")
    t = Text(Point(275, 250), 'Middle')
    t.setTextColor("white")
    t.setSize(11)
    t.draw(win)

    squares(425, 200, 525, 300, "grey33")
    t = Text(Point(475, 250), 'Right')
    t.setTextColor("white")
    t.setSize(11)
    t.draw(win)

    t = Text(Point(125, 400), 'NONE of the above =>')
    t.setTextColor("white")
    t.setSize(11)
    t.draw(win)

    p1 = Point(225, 350)
    p2 = Point(325, 450)
    a = Rectangle(p1, p2)
    a.setFill("grey33") 
    a.setOutline("white")
    a.draw(win)
    x1 = a.getP1().getX()
    y1 = a.getP1().getY()
    x2 = a.getP2().getX()
    y2 = a.getP2().getY()
    p = win.getMouse()   

    

    if x1 <= p.getX() <= x2 and y1 <= p.getY() <= y2:
                
        squares(0, 0, 275, 500, "green")
        t2 = Text(Point(130,200), '''
        You are correct! The right answer was:
        "NONE of the above"
        
        Did you get it in
        your first try?

        If you are still confused, let me
        explain it to you.
        As the instructions said,
        you had to select where The White House
        is located.

        The White House of the United states is
        located in Central Washington, D.C.
        Don't let the riddle distract you
        from the REAL question.
        
        Click anywhere to go 
        to the next puzzle! ''')
        t2.setTextColor("black")
        t2.setSize(10)
        t2.draw(win)
        
     
    else:
        r = Rectangle(Point(150, 175), Point(440, 250)) 
        r.setFill("black") 
        r.setWidth(1)
        r.setOutline("white")
        r.draw(win)

        t = Text(Point(275,200), '''WRONG!
        Click anywhere to try again''')
        t.setTextColor("red")
        t.setSize(13)
        t.draw(win)

        win.getMouse()
        t.undraw()
        r.undraw()
        puzzle_2()

def End():

    squares(0, 0, 550, 500, "yellow")

    t = Text(Point(275,200), '''THE END!
    Thank you for playing!!!!.
    Click anywhere to close the game.''')
    t.setTextColor("black")
    t.setSize(13)
    t.draw(win)
    
  
def main():

    intro()       
    puzzle_1()

    win.getMouse()
    puzzle_2()

    win.getMouse()
    End()
                
               
    win.getMouse()
    win.close()

main()