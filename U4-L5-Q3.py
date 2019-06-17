from turtle import *

Ryan = Turtle()

Ryan.color("blue")
Ryan.pensize(12)
Ryan.speed(9)
Ryan.shape("turtle")

def hexagon():
for x in range(6):
Ryan.forward(30)
Ryan.left(60) 

hexagon()
mainloop()