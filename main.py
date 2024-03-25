from turtle import Turtle , Screen

tim=Turtle()
screen=Screen()
tim.speed(0)
def move_fd():
    tim.fd(10)
    
def move_bc():
    tim.back(10)
    
def right():
    tim.right(10)
    
def circle():
    tim.circle(50)
  

def left():
    tim.left(10)
      
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

    
def undo():
    tim.undo()

readme="""
Guess the Up buton to forwards 10 steps
      the Down buton to backwards 10 steps
      the right buton to turn right by 10 degrees
      the left buton to turn left by 10 degrees
      the "c" to draw a circle
      the "d" to clear and reset game
      the "u" to undo the draw
"""

print(readme)

screen.onkey(move_fd, key="Up")
screen.onkey(move_bc,key="Down")
screen.onkey(right,"Right")
screen.onkey(left,"Left")
screen.onkey(circle,"c")
screen.onkey(clear,"d")
screen.onkey(undo,"u")
screen.listen()
screen.mainloop()