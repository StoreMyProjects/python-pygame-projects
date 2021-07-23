import pygame
import sys
import random

class Snake():
    def __init__(self):
        self.length = 1       #setting initial length of snake to 1
        self.positions = [((screen_width//2),(screen_height//2))]
        self.direction = random.choice([up,down,left,right])
        self.color = (17,24,47)       #setting snake color
        self.score = 0        #setting initial score to 0

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x,y = self.direction
        new = (((cur[0]+(x*gridsize))% screen_width), (cur[1]+(y*gridsize))% screen_height)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0,new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1           #reseting snake length to 1 after losing
        self.positions = [((screen_width//2), (screen_height//2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0

    def draw(self,surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (gridsize,gridsize))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (90,210,220), r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #whenever a key is pressed down
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)

class Food():
    def __init__(self):
        self.position = (0,0)
        self.color = (255,100,100)       #setting food color
        self.randomize_position()

    def randomize_position(self):        #positions of food would be random
        self.position = (random.randint(0,grid_width-1)*gridsize, random.randint(0,grid_height-1)*gridsize)

    def draw(self,surface):
        r = pygame.Rect((self.position[0], self.position[1]), (gridsize,gridsize))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (90,210,220), r, 1)

def drawgrid(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x+y)%2 == 0:
                r = pygame.Rect((x * gridsize, y * gridsize), (gridsize,gridsize))
                pygame.draw.rect(surface, (202,255,112), r)
                #pygame.draw.rect(surface, (180,0,180), r)
            else:
                rr = pygame.Rect((x * gridsize,y * gridsize), (gridsize,gridsize))
                pygame.draw.rect(surface, (188,238,104), rr)
                #pygame.draw.rect(surface, (150,0,150), rr)

screen_width = 600    #should be a multiple of 12
screen_height = 600

gridsize = 20
grid_width = screen_width//gridsize         #30
grid_height = screen_height//gridsize        #30

up = (0,-1)
down = (0,1)
left = (-1,0)
right = (1,0)

def main():
    pygame.init()                #initializing pygame
    
    #frames per second controller
    clock = pygame.time.Clock()
    #create display surface object
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
    pygame.display.set_caption('SNAKE')
    
    #create surface with same size as the window screen
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawgrid(surface)

    snake = Snake()
    food = Food()

    myfont = pygame.font.SysFont("monospace",20)


    while True:
        clock.tick(10)
        snake.handle_keys()
        drawgrid(surface)
        snake.move()
        
        if snake.get_head_position() == food.position:        #if snake eats food
            snake.length += 1                 #increase length of snake by 1
            snake.score += 1            #increase score by 1
            food.randomize_position()
            
        snake.draw(surface)
        food.draw(surface)
        #overlap the surface on window screen
        screen.blit(surface, (0,0))
        #draw score text over surface
        text = myfont.render("score: {0}".format(snake.score), 1, (139,69,0))
        screen.blit(text, (5,10))
        #refresh screen
        pygame.display.update()

main()
