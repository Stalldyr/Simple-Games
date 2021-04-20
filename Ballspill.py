from random import randint
from math import *
from graphics import *
from datetime import datetime


#Calculates the distance between two points
def distance(x1,x2,y1,y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)

#Creates a point with random coordinates
def random_coordinate(x_min, x_max, y_min, y_max):
    x = randint(x_min,x_max)
    y = randint(y_min,y_max)
    return(Point(x,y))

#Modifies a text-input and returns it
def text(text,x,y):
    text = Text(Point(x,y),text)
    text.setSize(25)
    text.setStyle("italic")
    return text

#Creates a window
def window(x,y):
    win = GraphWin("Target game",x,y)
    win.setBackground("white")
    return win

#Checks if a point is inside one of the targets. Ends the game if you hit the anti-target.
def is_point_inside(point,center,anti_center, radius,win):
    x = point.getX()
    y = point.getY()
    cx = center.getX()
    cy = center.getY()
    acx = anti_center.getX()
    acy = anti_center.getY()

    if distance(x,cx,y,cy)<radius:
        return True
    elif distance(x,acx,y,acy)<radius:
        game_over = text("GAME OVER",300,200)
        game_over.draw(win)
        return sqrt(-1)
    else:
        return False

#Draws the targets and counts the number of misses before the real target gets hit.
def draw_and_count(win, center, anti_center, radius):
    misses = 0
    
    target = Circle(center,radius)
    target.setFill("red")
    target.setOutline("red")
    target.draw(win)

    anti_target = Circle(anti_center,radius)
    anti_target.setFill(color_rgb(180,0,0))
    anti_target.setOutline(color_rgb(180,0,0))
    anti_target.draw(win)
    while is_point_inside(win.getMouse(),center,anti_center,radius,win) == False:
        misses +=1
    target.undraw()
    anti_target.undraw()
    return misses

#Creates n number of targets that make up the round.
def run_game_round(win, n, x_win, y_win):
    misses = 0
    target_size = 50
    start = datetime.now()

    for i in range(n):
        radius = target_size - (5*i)
        center = random_coordinate(radius, x_win-radius, radius, y_win-radius)
        anti_center = random_coordinate(radius, x_win-radius, radius, y_win-radius)
        cx = center.getX()
        cy = center.getY()
        acx = anti_center.getX()
        acy = anti_center.getY()
        while distance(cx,acx,cy,acy) < 2*radius:
            center = random_coordinate(radius, x_win-radius, radius, y_win-radius)
            anti_center = random_coordinate(radius, x_win-radius, radius, y_win-radius)
            cx = center.getX()
            cy = center.getY()
            acx = anti_center.getX()
            acy = anti_center.getY()
            
        misses += draw_and_count(win,center,anti_center, radius)   
    stop = datetime.now()
    delta = stop - start
    return (delta, misses)

#The main-function that starts and ends the game. 
def main():
    x_win, y_win = 600,400
    n = 10
    win = window(x_win, y_win)
    game = run_game_round(win, n, x_win, y_win )
    result = game[0].total_seconds() + game[1]
    score = text("Your score: " + str(result),300,300)
    score.draw(win)
    if result < 10:
        victory = text("You WIN!",300,200)
        victory.draw(win)
    else:
        loss = text("You lose...",300,200)
        loss.draw(win)

main()