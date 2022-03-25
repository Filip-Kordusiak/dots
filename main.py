from turtle import Turtle, Screen
import random

# tommy = Turtle()
# tommy.shape("turtle")
# tommy.color("red")
# tommy.speed(10)
# kolory= ["red","green","blue","orange","black"]
# kierunki = [0,90,180,270]
# xd=0
# for _ in range(36):
#     tommy.circle(99)
#     tommy.color(random.choice(kolory))
#     xd += 10
#     tommy.setheading(xd)
#
#
#
#
#
kolory = ["red","green","blue"]
tommy = Turtle()
tommy.hideturtle()
tommy.penup()
tommy.setheading(225)
tommy.forward(300)
tommy.setheading(0)
tommy.speed("fastest")
numerKropek=100

for dots in range(1, numerKropek+1):
    tommy.dot(20, random.choice(kolory))
    tommy.forward(50)

    if dots % 10 == 0:
        tommy.setheading(90)
        tommy.forward(50)
        tommy.setheading(180)
        tommy.forward(500)
        tommy.setheading(0)





# def ksztalt(boki):
#     for _ in range(boki):
#         tommy.forward(100)
#         tommy.right(360/boki)
#
#
# for liczbaBokow in range(3,11):
#     tommy.color(random.choice(kolory))
#     ksztalt(liczbaBokow)
#

#i = 4
#for i in range(10):
#    for _ in range(i):
#        nkat = 360/i
#        tommy.forward(100)
#        tommy.right(nkat)







screen = Screen()
screen.exitonclick()


