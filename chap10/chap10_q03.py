# Question 3 of Chapter 10
# draw a second housing for another set of traffic lights. Create three
# separate turtles to represent each of the green, orange and red lights, and position them appropriately
# within your new housing. As your state changes occur, just make one of the three turtles visible at
# any time.
import turtle           # Tess becomes a traffic light.

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
green = turtle.Turtle()
orange = turtle.Turtle()
red = turtle.Turtle()

def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    green.pensize(3)
    green.color("black", "darkgrey")
    green.begin_fill()
    green.forward(80)
    green.left(90)
    green.forward(200)
    green.circle(40, 180)
    green.forward(200)
    green.left(90)
    green.end_fill()


draw_housing()

green.penup()
# Position green onto the place where the green light should be
green.forward(40)
green.left(90)
green.forward(50)
# Turn green into a big green circle
green.shape("circle")
green.shapesize(3)
green.fillcolor("green")

orange.hideturtle()
orange.penup()
orange.forward(40)
orange.left(90)
orange.forward(120)
orange.shape("circle")
orange.shapesize(3)
orange.fillcolor("orange")

red.hideturtle()
red.penup()
red.forward(40)
red.left(90)
red.forward(190)
red.shape("circle")
red.shapesize(3)
red.fillcolor("red")

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red.  We number these states  0, 1, 2
# When the machine changes state, we change green' position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0

def advance_state_machine():
    global state_num
    if state_num == 0:       # Transition from state 0 to state 1
        orange.showturtle()
        green.hideturtle()
        state_num = 1
    elif state_num == 1:     # Transition from state 1 to state 2
        red.showturtle()
        orange.hideturtle()
        state_num = 2
    else:                    # Transition from state 2 to state 0
        green.showturtle()
        red.hideturtle()
        state_num = 0

    # Bind the event handler to a timer.
    wn.ontimer(advance_state_machine, 1000)

# Bind the event handler to the space key.
# wn.onkey(advance_state_machine, "space")

advance_state_machine()
wn.listen()                      # Listen for events
wn.mainloop()