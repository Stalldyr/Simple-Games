from random import choice
from graphics import *
from time import sleep

#Kills/ressurects it a cell if you hav clicked inside of it
def box_is_inside(point,board):
    click_x =  point.getX()
    click_y =  point.getY()

    x = int (click_x)
    y = int (click_y)

    if(board[x][y] == True):
        board[x][y] = False
    else:
        board[x][y] = True

    changes = [(x,y)]

    return (board, changes)

#Clears the board of cells
def clear_board():
    new_board = []
    changes = []
    for i in range(size()):
        row = []
        for j in range(size()):
            changes.append([i,j])
            row.append(False)
        new_board.append(row)

    return (0, new_board, changes)

#Checks if you have clicked inside a box
def clicked_box(point):
    click_x = point.getX()
    click_y = point.getY()

    if(0 < click_x < size()):
        if(0 < click_y < size()):
           return True

    return False

#Draws the buttons and returns each buttons midpoint
def draw_buttons(win):
    button_name = ["Start","Clear","Random","Load","Save","Quit"]
    button_midpoint = []
    for i in range(6):
        x = 0.1*size()+(i*2)
        y = -1.5
        midpoint = Point(x,y)
        button_midpoint.append(midpoint)

        button = Rectangle(Point(x-1,y-0.5),Point(x+1,y+0.5))
        button.draw(win)

        button_text = Text(Point(x,y),button_name[i])
        button_text.setSize(8)
        button_text.draw(win)

    return button_midpoint

#Creates a random board and draws it accordingly.
def initiate(win):
    board = []
    rectangles=[]
    
    for i in range(size()):
        row_random = []
        row_rectangles = []
        for j in range (size()):
            rectangle = Rectangle(Point(i,j),Point(i+1,j+1))
            row_rectangles.append(rectangle)
            rectangle.draw(win)
            
            row_random.append(random_bit())

        rectangles.append(row_rectangles)
        board.append(row_random)

    
    for x in range(size()):
        for y in range(size()):
            update_color(x, y, board, rectangles)
    
    
    return(board,rectangles)

#Checks if you have clicked one of the buttons.
def is_inside(rectangle,point):
    
    click_x = point.getX()
    click_y = point.getY()


    x = rectangle.getX()
    y = rectangle.getY()

    if((x-1) < click_x < (x+1)):
        if((y-0.5)< click_y < (y+0.5)):
           return True
    else:
        return False
    
#Iterates the board according to the game rules
def iterate(board):
    new_board = []
    changes = []
    living = 0
    
    for i in range(size()):
        row = []

        for j in range (size()):
            neighbours = living_neighbours(i,j,board)

            if board[i][j] == True:
                if neighbours < 2:
                    row.append(False)
                    changes.append([i,j])
                    
                elif neighbours == 2 or neighbours == 3:
                    row.append(True)
                    living += 1
                    
                elif neighbours > 3:
                    row.append(False)
                    changes.append([i,j])

            elif neighbours == 3:
                row.append(True)
                living += 1
                changes.append([i,j])
            else:
                row.append(False)

        new_board.append(row)
        
    return (living, new_board, changes)

#Counts have many surrounding living cells a cell has.
def living_neighbours(x,y,board):

    neighbours = 0

    for i in range(-1,2):
        for j in range(-1,2):
            v_x = x+i
            v_y = y+j            
            
            if (i == 0 and j == 0):
                pass
            
            elif (v_x < 0 or v_y < 0 or v_x == size() or v_y == size()):
                if board[v_x%size()][v_y%size()] == True:
                    neighbours +=1
                
            elif board[v_x][v_y] == True:
                neighbours += 1
                
    return neighbours

#Returns a random value of True or False.
def random_bit():
    return choice([True,False])

#Defines the size of the game
def size():
    n = 20

    return n

#Updates the board for each change.
def update_board(board,changes,rectangles):
    for i in range(len(changes)):
        update_color(changes[i][0], changes[i][1], board, rectangles)

#Updates the color for each change
def update_color(x, y, board, rectangles):
    if (board[x][y]):
        rectangles[x][y].setFill("red4")
    else:
        rectangles[x][y].setFill("gray3")


#Main function of the game
def game_of_life():
    win=GraphWin("Game of Life",500,600)
    win.setCoords(0,-3,size(),size())
    board,rectangles = initiate(win)
    buttons = draw_buttons(win)

    label = Entry(Point(size()-1,-1.5),4)
    label.draw(win)

    while(True):

        if clicked_box(win.getMouse()) == True:
            board,changes = box_is_inside(win.getMouse(),board)
            update_board(board,changes,rectangles)
        
        elif is_inside(buttons[0],win.getMouse()) == True:
            n = label.getText()
            if n == "":
                n = 1
            else:
                n = int(n)
            
            for i in range(n):
                living, board, changes = iterate(board)
                update_board(board,changes,rectangles)
                sleep(1)

        elif is_inside(buttons[1],win.getMouse()) == True:
            living, board, changes = clear_board()
            update_board(board,changes,rectangles)

        elif is_inside(buttons[2],win.getMouse()) == True:
            initiate(win)

        elif is_inside(buttons[3],win.getMouse()) == True:
            load_file = open("save.txt","r")
            board = []

            board = eval(load_file.readline())
            changes = []

            for x in range(size()):
                for y in range(size()):
                    changes.append([x,y])

            update_board(board, changes, rectangles)

        elif is_inside(buttons[4],win.getMouse()) == True:
            save_file = open("save.txt","w")
            print(board, file = save_file)
            save_file.close()


        elif(is_inside(buttons[5],win.getMouse()) == True):
            win.close()
            break
            

game_of_life()
