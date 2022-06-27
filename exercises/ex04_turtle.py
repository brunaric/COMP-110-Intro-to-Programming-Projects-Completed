"""A Forest at Night."""

__author__ = "730466477"

from turtle import Turtle, colormode, done
import random
colormode(255)


def main() -> None: 
    """The entry point of my scene. Lines 16-17 include something extra I implemented using random and lists."""
    mt: Turtle = Turtle()
    tt: Turtle = Turtle()
    rt: Turtle = Turtle()
    st: Turtle = Turtle()
    list1: list[int] = [-125, -80, 0, 100, 180, 250]
    list2: list[int] = [0, 50, 100, 175, 200]
     
    moon(mt, -200, 150)
    triangle(tt, -150, -150)
    rectangle(rt, -100, -250)
    star(st, 150, 150)
    i: int = 0 
    while i < 3:
        star(st, random.choice(list1), random.choice(list2))
        i += 1
        
    done()


def moon(mt: Turtle, x: float, y: float) -> None:
    """Trying something fun: Draws the moon in the sky in the shape of a circle (Lines 46-47)."""
    mt.penup()
    mt.goto(x, y)
    mt.pendown 

    MAX_SPEED: int = 0 
    mt.speed(MAX_SPEED)

    mt.color(255, 254, 200)
    mt.begin_fill()
    mt.fillcolor(255, 254, 200)

    i: int = 0
    while(i < 2):
        r = 48
        mt.circle(r)  
        i += 1
    mt.end_fill()


def star(st: Turtle, x: float, y: float) -> None:
    """Draws star in the sky."""    
    st.penup()
    st.goto(x, y)
    st.pendown()

    MAX_SPEED: int = 0
    st.speed(MAX_SPEED)

    st.color(252, 249, 69)
    st.begin_fill()
    st.fillcolor(252, 249, 69)

    i: int = 0
    while i < 5:
        st.forward(50)
        st.left(145)
        i = i + 1
    st.end_fill()


def triangle(tt: Turtle, x: float, y: float) -> None:
    """Draws top part of the tree."""
    tt.penup()
    tt.goto(x, y)
    tt.pendown()

    MAX_SPEED: int = 0
    tt.speed(MAX_SPEED)

    tt.color(0, 147, 79)
    tt.begin_fill()
    tt.fillcolor(0, 147, 79)

    i: int = 0
    while i < 3:
        tt.forward(200)
        tt.left(120)   
        i += 1
    tt.end_fill()


def rectangle(rt: Turtle, x: float, y: float) -> None:
    """Draws bottom part of the tree."""
    rt.penup()
    rt.goto(x, y)
    rt.pendown()

    MAX_SPEED: int = 0
    rt.speed(MAX_SPEED) 
    
    rt.color(111, 78, 17)
    rt.begin_fill()
    rt.fillcolor(111, 78, 17)
    
    i: int = 0
    while i < 4:
        rt.forward(100)
        rt.left(90)   
        i += 1
    rt.end_fill()


if __name__ == "__main__":   
    main() 
