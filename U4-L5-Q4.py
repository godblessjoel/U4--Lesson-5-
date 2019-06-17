from turtle import *

Ryan = Turtle()

Ryan.color("blue")
Ryan.pensize(12)
Ryan.speed(9)
Ryan.shape("turtle")

def hexagon(s):
for x in range(6):
Ryan.forward(s)
Ryan.left(60) 

for x in range(10,200,20):
hexagon(x)

mainloop()