# Question 5 of Chapter 10
# Four states: Green(3s), 
#              Green + Orange(1s), 
#              Orange(1s), 
#              Red(2s).
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
green.fillcolor("grey")

orange.penup()
orange.forward(40)
orange.left(90)
orange.forward(120)
orange.shape("circle")
orange.shapesize(3)
orange.fillcolor("grey")

red.penup()
red.forward(40)
red.left(90)
red.forward(190)
red.shape("circle")
red.shapesize(3)
red.fillcolor("grey")

# This variable holds the current state of the machine
state_num = 0
sec = 0

def advance_state_machine():
    global state_num
    global sec
    if state_num == 0:       # Transition from state 0 to state 1
        red.fillcolor("grey")
        green.fillcolor("green")
        state_num = 1
        sec = 3000
    elif state_num == 1:     # Transition from state 1 to state 2
        orange.fillcolor("orange")
        state_num = 2
        sec = 1000
    elif state_num == 2:     # Transition from state 2 to state 3
        green.fillcolor("grey")
        state_num = 3
    else:                    # Transition from state 3 to state 0
        orange.fillcolor("grey")
        red.fillcolor("red")
        state_num = 0
        sec = 2000

    # Bind the event handler to a timer.
    wn.ontimer(advance_state_machine, sec)

# Bind the event handler to the space key.
# wn.onkey(advance_state_machine, "space")

advance_state_machine()
wn.listen()                      # Listen for events
wn.mainloop()