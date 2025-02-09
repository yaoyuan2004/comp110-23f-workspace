"""turtle_tutorial"""
__author__ = "730713462"
from turtle import Turtle, colormode, done


def sun(t: Turtle, x: float, y: float) -> None:
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(50)
    t.end_fill()


def mounten(t: Turtle, x: float, y: float) -> None:
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("gray")
    t.begin_fill()
    for i in range(3):
        t.forward(300)
        t.left(120)
    t.end_fill()

    
def house(t: Turtle, x: float, y: float) -> None:
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("blue")
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()
    t.penup()
    t.goto(x-20,y+100)
    t.pendown()
    t.pencolor("black")
    t.fillcolor("red")
    t.begin_fill()
    for idx in range(3):
        t.forward(140)
        t.left(120)
    t.end_fill()


def flag(t: Turtle, x: float, y: float) -> None:
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("black")
    t.left(90)
    t.forward(180)
    t.fillcolor("orange")
    t.begin_fill()
    for idx in range(3):
        t.forward(60)
        t.right(120)
    t.end_fill()


def main() -> None:
    t: Turtle = Turtle()
    sun(t,220,250)
    for i in range(-2,2):
        mounten(t,140*i,50)
    house(t,-200,-120)
    flag(t,-50,-130)
    done()


if __name__ == "__main__":
    main()