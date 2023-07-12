import turtle
import time
import sys
from DataStructures import Queue, ExploredSet

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("A BFS Maze Solving Program")
wn.setup(1300, 700)


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
        self.penup()
        self.speed(0)


# use the yellow turtle to represent the end position and the solution path
class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)


grid = [
    "+++++++++++++++++++++++++++++++++++++++++++++++++++",
    "+               +                                 +",
    "+  ++++++++++  +++++++++++++  +++++++  ++++++++++++",
    "+s          +                 +               ++  +",
    "+  +++++++  +++++++++++++  +++++++++++++++++++++  +",
    "+  +     +  +           +  +                 +++  +",
    "+  +  +  +  +  +  ++++  +  +  +++++++++++++  +++  +",
    "+  +  +  +  +  +  +        +  +  +        +       +",
    "+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
    "+  +     +  +          +   +           +  +  ++  ++",
    "+  ++++  +  +++++++ ++++++++  +++++++++++++  ++  ++",
    "+     +  +     +              +              ++   +",
    "++++  +  ++++++++++ +++++++++++  ++++++++++  +++  +",
    "+  +  +                    +     +     +  +  +++  +",
    "+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
    "+  +  +     +     +     +  +  +     +     +  ++  ++",
    "+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
    "+                       +  +  +              ++  ++",
    "+ ++++++             +  +  +  +  +++        +++  ++",
    "+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
    "+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
    "+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
    "+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
    "+      ++ +++++++e+++     ++          ++    +++++++",
    "+++++++++++++++++++++++++++++++++++++++++++++++++++",
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

            if character == " " or character == "e":
                path.append((screen_x, screen_y))

            if character == "e":
                green.color("purple")
                green.goto(screen_x, screen_y)
                end_x, end_y = screen_x, screen_y
                green.stamp()
                green.color("green")

            if character == "s":
                start_x, start_y = screen_x, screen_y
                red.goto(screen_x, screen_y)


def endProgram():
    wn.exitonclick()
    sys.exit()


def search(x, y): # Args: x, y are the starting position of the search 
    fringe.enqueue((x, y)) # add the starting position to the queue
    solution[(x, y)] = (x, y)

    while len(fringe) > 0:
        time.sleep(0)
        x, y = fringe.dequeue() # remove the first element from the queue 

        if (x - 24, y) in path and (x - 24, y) not in visited: # Valid path and not visited ? (Left cell)
         cell = (x - 24, y) 
         solution[cell] = x, y # Add the current cell to the solution dictionary
         blue.goto(cell)
         blue.stamp()
         fringe.enqueue(cell)
         visited.add((x - 24, y))

        if (x, y - 24) in path and (x, y - 24) not in visited: # Valid path and not visited ? (Down cell)
            cell = (x, y - 24)
            solution[cell] = (x, y)
            blue.goto(cell)
            blue.stamp()
            fringe.enqueue(cell)
            visited.add((x, y - 24))

        if (x + 24, y) in path and (x + 24, y) not in visited: # Valid path and not visited ? (Right cell)
            cell = (x + 24, y)
            solution[cell] = (x, y)
            blue.goto(cell)
            blue.stamp()
            fringe.enqueue(cell)
            visited.add((x + 24, y))

        if (x, y + 24) in path and (x, y + 24) not in visited: # Valid path and not visited ? (Up cell)
            cell = (x, y + 24)
            solution[cell] = (x, y)
            blue.goto(cell)
            blue.stamp()
            fringe.enqueue(cell)
            visited.add((x, y + 24))
        
        if (x, y) != (start_x, start_y): # If the current cell is not the start cell
            green.goto(x, y)
            green.stamp()

        

def backRoute(x, y):
    yellow.goto(x, y)
    yellow.stamp()
    while (x, y) != (start_x, start_y): # While the current cell is not the start cell
        yellow.goto(solution[x, y]) # Go to the next cell in the solution dictionary
        yellow.stamp()
        x, y = solution[x, y] # Update the current cell to the next cell in the solution dictionary


maze = Maze()
red = Red()
blue = Blue()
green = Green()
yellow = Yellow()

walls = []
path = []
visited = ExploredSet()
fringe = Queue()
solution = {}

setup_maze(grid)
search(start_x, start_y)
backRoute(end_x, end_y)
wn.exitonclick()
