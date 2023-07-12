import turtle
import time
import sys
from DataStructures import Stack, ExploredSet

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("A DFS Maze Solving Program")
wn.setup(1300, 700)

# declare system variables
start_x = 0
start_y = 0
end_x = 0
end_y = 0


class Maze(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)


# use green turtles to show the visited cells
class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)


# use blue turtle to show the frontier cells
class Blue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)


# use the red turtle to represent the start position
class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.setheading(270)  # point turtle to point down
        self.penup()
        self.speed(0)


# use the yellow turtle to represent the solution path
class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)


# use the orange turtle to represent the end position
class Orange(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("orange")
        self.penup()
        self.speed(0)


grid1 = [
    "++++++++++++++++++++++++++++++++++++++++++++++",
    "+ s             +                            +",
    "+ +++++++++++ +++++++++++++++ ++++++++ +++++ +",
    "+           +                 +        +     +",
    "++ +++++++ ++++++++++++++ ++++++++++++++++++++",
    "++ ++    + ++           + ++                 +",
    "++ ++ ++ + ++ ++ +++++ ++ ++ +++++++++++++++ +",
    "++ ++ ++ + ++ ++ +     ++ ++ ++ ++        ++ +",
    "++ ++ ++++ ++ +++++++++++ ++ ++ +++++ +++ ++ +",
    "++ ++   ++ ++             ++          +++ ++e+",
    "++ ++++ ++ +++++++++++++++++ +++++++++++++++ +",
    "++    + ++                   ++              +",
    "+++++ + +++++++++++++++++++++++ ++++++++++++ +",
    "++ ++ +                   ++          +++ ++ +",
    "++ ++ ++++ ++++++++++++++ ++ +++++ ++ +++ ++ +",
    "++ ++ ++   ++     +    ++ ++ ++    ++     ++ +",
    "++ ++ ++ +++++++ +++++ ++ ++ +++++++++++++++ +",
    "++                     ++ ++ ++              +",
    "+++++ ++ + +++++++++++ ++ ++ ++ ++++++++++++++",
    "++++++++++++++++++++++++++++++++++++++++++++++",
]


def setup_maze(grid):
    global start_x, start_y, end_x, end_y
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            character = grid[y][x]
            screen_x = -588 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "+":
                maze.goto(screen_x, screen_y)
                maze.stamp()
                walls.append((screen_x, screen_y))

            if character == " ":
                path.append((screen_x, screen_y))

            if character == "e":
                yellow.goto(screen_x, screen_y)
                yellow.stamp()
                end_x, end_y = screen_x, screen_y
                path.append((screen_x, screen_y))

            if character == "s":
                start_x, start_y = screen_x, screen_y
                red.goto(screen_x, screen_y)


def endProgram():
    wn.exitonclick()
    sys.exit()


def search(x, y):
    fringe.push((x, y))
    solution[(x, y)] = (x, y)

    while not fringe.is_empty():
        time.sleep(0)
        x, y = fringe.pop()

        if (x - 24, y) in path and (x - 24, y) not in visited:
            cellleft = (x - 24, y)
            solution[cellleft] = (x, y)
            blue.goto(cellleft)
            blue.stamp()
            fringe.push(cellleft)
            visited.add(cellleft)

        if (x, y - 24) in path and (x, y - 24) not in visited:
            celldown = (x, y - 24)
            solution[celldown] = (x, y)
            blue.goto(celldown)
            blue.stamp()
            fringe.push(celldown)
            visited.add(celldown)

        if (x + 24, y) in path and (x + 24, y) not in visited:
            cellright = (x + 24, y)
            solution[cellright] = (x, y)
            blue.goto(cellright)
            blue.stamp()
            fringe.push(cellright)
            visited.add(cellright)

        if (x, y + 24) in path and (x, y + 24) not in visited:
            cellup = (x, y + 24)
            solution[cellup] = (x, y)
            blue.goto(cellup)
            blue.stamp()
            fringe.push(cellup)
            visited.add(cellup)

        green.goto(x, y)
        green.stamp()

        if (x, y) == (end_x, end_y):
            orange.goto(x, y)
            orange.stamp()

        if (x, y) == (start_x, start_y):
            red.stamp()


def backRoute(x, y):
    yellow.goto(x, y)
    yellow.stamp()
    while (x, y) != (start_x, start_y):
        yellow.goto(solution[x, y])
        yellow.stamp()
        x, y = solution[x, y]


maze = Maze()
red = Red()
blue = Blue()
green = Green()
yellow = Yellow()
orange = Orange()
walls = []
path = []
visited = ExploredSet()
fringe = Stack()
solution = {}

setup_maze(grid1)
search(start_x, start_y)
backRoute(end_x, end_y)

wn.exitonclick()
