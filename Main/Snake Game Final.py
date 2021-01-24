from microbit import *
from random import randint

class Snake:
    """ This class contains the functions that operate
        on our game as well as the state of the game.
        It's a handy way to link the two.
    """

    def __init__(self):
        """ Special function that runs when you create
            a "Snake", ie. when you run
                game = Snake()
            init stands for "Initialisation"
        """
        ## UNCOMMENT AND FILL IN THE # LINES BELOW WITH START VALUES
        ## current direction is a string with up, down, left or right
        self.current_direction = "up"
        ## snake is a list of the pixels that the snake is at
        self.snake = [[2, 2]]
        ## food is the co-ords of the current food
        self.food = [1,1]
        ## whether or not to end the game, used after update
        self.end = False
        pass

    def handle_input(self):
        """ We'll use this function to take input from the
            user to control which direction the snake is going
            in.
        """
        x = accelerometer.get_x();
        y = accelerometer.get_y();
        
        if abs(x)>abs(y):
            if x > 0:
                self.current_direction = "right"
            else: 
                self.current_direction = "left"
        else:
            if y > 0:
                self.current_direction = "down"
            else: 
                self.current_direction = "up"
        
        pass

    def update(self):
        """ This function will update the game state
            based on the direction the snake is going.
        """
        # The line below makes a copy of the head of the snake
        # you will be working with that copy in this function
        new_head = list(self.snake[-1])
        
        if self.current_direction == "up":
            new_head[1] = new_head[1] - 1
        elif self.current_direction == "down":
            new_head[1] = new_head[1] + 1
        elif self.current_direction == "right":
            new_head[0] = new_head[0] + 1
        else: # else is left
            new_head[0] = new_head[0] - 1
            
        if new_head[0] == 5:
            new_head[0] = 0
        elif new_head[0] == -1:
            new_head[0] = 4
        elif new_head[1] == 5:
            new_head[1] = 0
        elif new_head[1] == -1:
            new_head[1] = 4
        
        
        
        
        if new_head == self.food:                           # if snake eats food
            self.food = [randint(0,4),randint(0,4)]
            while self.food in self.snake:
                self.food = [randint(0,4),randint(0,4)]  
                
            self.snake.append(new_head)
                             
        else:                                               # doesn't eat food, doesn't extend in length, could clash
            if new_head in self.snake:                          # clash function
                self.end = True
            else:
                self.snake.append(new_head)
                self.snake = self.snake[1:]
                
        
        
            
        pass

    def draw(self):
        """ This makes the game appear on the LEDs. """
        display.clear()
        display.set_pixel(self.food[0], self.food[1], 5)
        for part in self.snake:
            display.set_pixel(part[0], part[1], 9)

# game is an "instance" of Snake
game = Snake()

# this is called our "game loop" and is where everything
# happens
while True:
    
    if game.end == True:
        display.show(Image.SAD)
        break
    else:
        game.handle_input()
        game.update()
        game.draw()
        # this makes our micro:bit do nothing for 500ms
        sleep(500)
