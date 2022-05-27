from turtle import Turtle, Screen
import time

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5)
        self.color('white')
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.05
        
    def move(self):
        self.goto( self.xcor() - self.move_x, self.ycor() - self.move_y)
        
    def bounce_y(self):
        self.move_y *= -1
        
    def bounce_x(self):
        self.move_x *= -1
        
    def reset_ball(self):
        self.goto(0,0)
        self.move_speed = 0.05
        self.move_x = 10
        self.move_y = 10
        
class Paddle(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('blue')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.goto(0,-250)
        
    def left(self):
        self.goto( self.xcor() - 20, self.ycor() )
        
    def right(self):
        self.goto( self.xcor() + 20, self.ycor() )

class Blocks():
    
    def __init__(self):
        self.blocks = []
        self.x_pos = [-180, -135, -90, -45, 0, 45, 90, 135, 180]
        self.y_pos = [130, 155, 180, 205, 230, 255]
        self.create_block()
    
    def create_block(self):
        for i in range(len(self.y_pos)):
            for j in range(len(self.x_pos)):
                self.block = Turtle()
                self.block.shape('square')
                if i < 2:
                    self.block.color('green') 
                elif i < 4:
                    self.block.color('yellow') 
                else:
                    self.block.color('red') 
                self.block.shapesize(stretch_wid=1, stretch_len=2)
                self.block.penup()
                self.block.goto(self.x_pos[j], self.y_pos[i])
                self.blocks.append(self.block)
    
    def delete(self, block):
        block.ht()
        self.blocks.remove(block)
            
class Board(Turtle):
    
    def __init__(self):
        super().__init__()
        self.live = 3
        self.ht()
        self.penup()
        self.color('white')
        self.goto(185,-290)
        self.write(f"{self.live}", font=('Arial', 18, 'normal'))
        
    def die(self):
        self.live -= 1
        self.clear()
        self.write(f"{self.live}", font=('Arial', 18, 'normal'))
        
    def game_over(self, win):
        self.goto(-50,0)
        if win == True:
            self.write(f"You Win!", font=('Arial', 18, 'normal'))
        else:
            self.write(f"You Lose!", font=('Arial', 18, 'normal'))


screen = Screen()
screen.setup(width=410, height=600)
screen.title("BreakOut")
screen.bgcolor('black')
game_on = True
screen.tracer(0)

user = Paddle()
ball = Ball()
blocks = Blocks()
board = Board()

screen.listen()
screen.onkeypress(key="Right", fun=user.right)
screen.onkeypress(key="Left", fun=user.left)

while game_on:
    
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    for block in blocks.blocks:
        if ball.distance(block) < 40:
            blocks.delete(block)
            ball.bounce_y()
            ball.move_speed *= 0.95
    
    if ball.distance(user) < 50 and ball.ycor() > -240 and ball.ycor() < -220:
        ball.bounce_y()
        
    if ball.xcor() > 180 or ball.xcor() < -180:
        ball.bounce_x()
    
    if ball.ycor() > 280:
        ball.bounce_y()
        
    if ball.ycor() < -300:
        board.die()
        ball.reset_ball()
        
    if board.live == 0:
        game_on = False
        board.game_over(False)
        
    if blocks.blocks == []:
        game_on = False
        board.game_over(True)
        
screen.exitonclick()