from turtle import *
from random import randint
wn = Screen()
wn.bgcolor("green")
hideturtle()
speed(22)
penup()
goto(-200,200)
step=0
for step in range(20):
    write(step)
    right(90)
    forward(10)
    pendown()
    forward(130)
    penup()
    backward(140)
    left(90)
    forward(25)
one=Turtle()
one.color('red')
one.shape('turtle')
one.penup()
one.goto(-220,170)
one.pendown()
two=Turtle()
two.color('yellow')
two.shape('turtle')
two.penup()
two.goto(-220,140)
two.pendown()
three=Turtle()
three.color('blue')
three.shape('turtle')
three.penup()
three.goto(-220,110)
three.pendown()
a=('winner')
goto(0,-10)
write(a)
addk=0
addkk=0
addkkk=0
for turn in range(180):
    k=randint(1,5)
    rd=randint(1,5)
    lmn=randint(1,5)
    one.forward(k)
    two.forward(rd)
    three.forward(lmn)
    addk+=k
    addkk+=rd
    addkkk+=lmn
    
    if addk>=500:
        one.penup()
        one.goto(0,10)
        break
    elif addkk>=500:
        two.penup()
        two.goto(0,10)
        break
    elif addkkk>=500:
        three.penup()
        three.goto(0,10)
        break

wn.mainloop()
