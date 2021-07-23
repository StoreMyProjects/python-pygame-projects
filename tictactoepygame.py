import pygame
import sys
import numpy as np

#initiate pygame and give permission to use pygame's functionality
pygame.init()

#assigning values to parameters
width = 500
height = 500
line_width = 15
board_rows = 3
board_cols = 3
square_size = width // board_cols
circle_radius = square_size//3
circle_width = 15
cross_width = 25
space = square_size // 4

#setting colors by defining RGB value
#bg_color = (28,170,156)
bg_color = (255,211,67)
#line_color = (23,145,135)
line_color = (139,131,120)
circle_color = (239,231,200)
cross_color = (66,66,66)

#create display surface object
screen = pygame.display.set_mode((width,height))
#set the pygame window name 
pygame.display.set_caption('TIC TAC TOE')
screen.fill(bg_color)

#board
board=np.zeros((board_rows,board_cols))

#drawing grids
def draw_lines():
    #1 horizontal line
    pygame.draw.line(screen,line_color,(0,square_size),(width,square_size),line_width)
    #2 horizontal line
    pygame.draw.line(screen,line_color,(0,2*square_size),(width,2*square_size),line_width)
    #1 vertical line
    pygame.draw.line(screen,line_color,(square_size,0),(square_size,height),line_width)
    #2 vertical line
    pygame.draw.line(screen,line_color,(2*square_size,0),(2*square_size,height),line_width)

#draw x and o
def draw_figures():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 1:
                pygame.draw.circle(screen,circle_color,(int(col *square_size+square_size//2),int(row *square_size+square_size//2)),circle_radius,circle_width)
            elif board[row][col] == 2:
                pygame.draw.line(screen,cross_color,(col*square_size+space,row*square_size+square_size-space),(col*square_size+square_size-space,row*square_size+space),cross_width)
                pygame.draw.line(screen,cross_color,(col*square_size+space,row*square_size+space),(col*square_size+square_size-space,row*square_size+square_size-space),cross_width)

def mark_square(row,col,player):
    board[row][col] = player

def available_square(row,col):
    return board[row][col] == 0

def is_board_full():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 0:
                return False
    
    return True

#checking for winner function
def check_winner(player):
    #vertical win check
    for col in range(board_cols):
        if board[0][col] == board[1][col] == board[2][col] == player:
            draw_ver_win_line(col,player)
            return True
    #horizontal win check
    for row in range(board_rows):
        if board[row][0] == board[row][1] == board[row][2] == player:
            draw_hori_win_line(row,player)
            return True
    #asc diagonal win check
    if board[2][0] == board[1][1] == board[0][2] == player:
        draw_asc_diag(player)
        return True
    #desc diagonal win check
    if board[0][0] == board[1][1] == board[2][2] == player:
        draw_desc_diag(player)
        return True
    
    return False

#creating win lines
def draw_ver_win_line(col,player):
    posX = col * square_size + square_size//2
    
    if player == 1:
        color = circle_color
    elif player ==2:
        color = cross_color
        
    pygame.draw.line(screen,color,(posX,15),(posX,height - 15),line_width)

def draw_hori_win_line(row,player):
    posY = row * square_size + square_size//2
    if player == 1:
        color = circle_color
    elif player ==2:
        color = cross_color
        
    pygame.draw.line(screen,color,(15,posY),(width - 15,posY),line_width)

def draw_asc_diag(player):
    if player == 1:
        color = circle_color
    elif player ==2:
        color = cross_color
        
    pygame.draw.line(screen,color,(15, height - 15),(width - 15 ,15),line_width)

def draw_desc_diag(player):
    if player == 1:
        color = circle_color
    elif player ==2:
        color = cross_color
        
    pygame.draw.line(screen,color,(15, 15),(width - 15 ,height - 15),line_width)

draw_lines()

#restart game function
def restart():
    screen.fill(bg_color)
    draw_lines()
    for row in range(board_rows):
        for col in range(board_cols):
            board[row][col] = 0

#setting first chance to player 1
player = 1
game_over = False

#main loop
while True:
    #iterate over the list of event objects
    for event in pygame.event.get():
        #quitting pygame and program both if event object type is quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            
            mouseX = event.pos[0] #x
            mouseY = event.pos[1] #y
            
            clicked_row = int(mouseY//square_size)
            clicked_col = int(mouseX//square_size)
            
            if available_square(clicked_row,clicked_col):
                mark_square(clicked_row,clicked_col,player)
                #check for winner
                if check_winner(player):
                    game_over = True
                #else switch player
                player = player % 2 + 1
                
                draw_figures()
                    
        if event.type == pygame.KEYDOWN:
            #press space key to restart
            if event.key == pygame.K_SPACE:
                restart()
                player = 1
                game_over = False
    #refresh screen            
    pygame.display.update()