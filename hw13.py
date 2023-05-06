#Problem A
import turtle, random

class Game:
    '''
    Purpose: The Game class sets up the instance variables and runs the snake game
    Instance variables: The game class sets up the turtle game board and runs the gameloop
    Methods: __init__() is the constructor and builds the turtle graphics
             gameloop() keeps the game running at a set speed while the snake is still in bounds and
                    kills the game to prints out "Game Over" when the snake goes out of the boundries
    '''

    def __init__(self):
        #Setup 700x700 pixel window
        turtle.setup(700, 700)

        #Bottom left of screen is (-40, -40), top right is (640, 640)
        turtle.setworldcoordinates(-40, -40, 640, 640)
        cv = turtle.getcanvas()
        cv.adjustScrolls()

        #Ensure turtle is running as fast as possible
        turtle.hideturtle()
        turtle.delay(0)
        turtle.speed(0)

        #Draw the board as a square from (0,0) to (600,600)
        for i in range(4):
            turtle.forward(600)
            turtle.left(90)

        self.food = Food()

        self.player = Snake(315, 315, 'blue')
        #self.enemy = Snake(15,15, 'purple')

        self.gameloop()

        turtle.onkeypress(self.player.go_down, 'Down')
        turtle.onkeypress(self.player.go_up, 'Up')
        turtle.onkeypress(self.player.go_left, 'Left')
        turtle.onkeypress(self.player.go_right, 'Right')
        turtle.listen()
        turtle.mainloop()




    def gameloop(self):
        if self.player.gameover() == False:
            self.player.move(self.food)
            #self.enemy.move(self.food)
            turtle.ontimer(self.gameloop, 200)
        else:
            turtle.setpos(0,250)
            turtle.write("Game Over :(", True, align="left",font=('Arial', 100, 'normal'))

            print('Game Over!!!!!!!!')

class Snake:
    '''
    Purpose: Creates the snake and allows it to move and eat the apples
    Instance variables: The constructor takes in self to allow variables to pass through, x and y which looks at
        the snakes location, and lastly the color which can be chosen
    Methods: __init__() is the constructor and sets the variables with self
             grow() allows the snake to grow when it eats an apple
             move() allows the snake to move and the other sections to follow
             gameover() is set to false until the snake passes the boundries and then ends the game
             go_down() sets the snake's velocity to down
             go_up() sets the snake's velocity to up
             go_left() sets the snake's velocity to left
             go_right() sets the snake's velocity to right
    '''

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.segments = []
        self.grow()
        self.vx = 30
        self.vy = 0



    def grow(self):
        head = turtle.Turtle()
        head.speed(0)
        head.fillcolor(self.color)
        head.shape('square')
        head.shapesize(1.5, 1.5, 1.5)
        head.penup()
        head.setpos(self.x, self.y)
        self.segments.append(head)


    def move(self, food):
        self.x += self.vx
        self.y += self.vy

        if self.x == food.fcorx and self.y == food.fcory:
            food.eaten()
            Snake.grow(self)
        else:
            for i in range(len(self.segments) - 1):
                x = self.segments[i+1].xcor()
                y = self.segments[i+1].ycor()
                self.segments[i].setpos(x, y)
            self.segments[-1].setpos(self.x, self.y)

    def gameover(self):
        #if 0 > self.x > 600 or 0 > self.y > 600:
        if self.x < 0 or self.x > 600 or self.y < 0 or self.y > 600:
            print('Oh No!')
            return True
        else:
            #print('x: ',self.x)
            #print('y: ',self.y)

            return False



    def go_down(self):
        self.vx = 0
        self.vy = -30

    def go_left(self):
        self.vx = -30
        self.vy = 0

    def go_up(self):
        self.vx = 0
        self.vy = 30

    def go_right(self):
        self.vx = 30
        self.vy = 0

class Food:
    '''
    Purpose: Creates the food that the snake can eat and grow
    Instance variables: Creates self which allows the food to be made and eaten
    Methods: __init__() Creates a turtle object and calls the create() method
             create() makes the apple and puts it in a random place on the game board
             eaten() is called when the snake head passes through the apple and clears the apple
                and calls the create class to draw up a new one
    '''

    def __init__(self):
        self.food = turtle.Turtle()
        self.create()
    def create(self):

        self.fcorx = 15 + 30*random.randint(0,19)
        self.fcory = 15 + 30*random.randint(0,19)
        self.food.speed(0)
        self.food.fillcolor('red')
        self.food.shape('circle')
        self.food.shapesize(1.5, 1.5, 1.5)
        self.food.penup()
        self.food.setpos(self.fcorx, self.fcory)

    def eaten(self):
        self.food.clear()
        self.create()



Game()
