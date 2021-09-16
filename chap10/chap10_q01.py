# Question 1 of Chapter 10
# Add some new key bindings:
# - Pressing keys R, G or B should change tess’s color to Red, Green or Blue.
# - Pressing keys + or - should increase or decrease the width of tess’s pen. 
#   Ensure that the pen size stays between 1 and 20 (inclusive).
# - 
import turtle

turtle.setup(400,500)                # Determine the window size
wn = turtle.Screen()                 # Get a reference to the window
wn.title("Handling keypresses!")     # Change the window title
wn.bgcolor("lightgreen")             # Set the background color
tess = turtle.Turtle()               # Create our favorite turtle

# The next four functions are our "event handlers".
def h1():
   tess.forward(30)

def h2():
   tess.left(45)

def h3():
   tess.right(45)

def h4():
    wn.bye()                        # Close down the turtle window

def red():
    tess.color("red")

def green():
    tess.color("green")

def blue():
    tess.color("blue")

def increase():
    size = tess.pensize()
    if size < 20:
        tess.pensize(size + 1)
        print("Pensize:{}".format(tess.pensize()))

def decrease():
    size = tess.pensize()
    if size > 1:
        tess.pensize(size - 1)
        print("Pensize:{}".format(tess.pensize()))

# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")

wn.onkey(red, "r")
wn.onkey(green, "g")
wn.onkey(blue, "b")

wn.onkey(increase, "+")
wn.onkey(decrease, "minus") # setting key as "-"" doesn't work.

# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()