import turtle

# Set up the turtle
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Thank You So Much")

# Create turtle object
pen = turtle.Turtle()
pen.speed(3)

# Function to draw a single letter
def draw_letter(letter, font_size=30):
    pen.penup()
    pen.write(letter, font=("Arial", font_size, "bold"))
    pen.forward(font_size)
    pen.pendown()

# Function to write "THANK YOU SO MUCH"
def draw_message():
    pen.penup()
    pen.goto(-300, 100)
    pen.pendown()

    # Drawing "THANK"
    for letter in "THANK":
        draw_letter(letter)

    # Move turtle to the next line
    pen.penup()
    pen.goto(-300, 50)
    pen.pendown()

    # Drawing "YOU"
    for letter in "YOU":
        draw_letter(letter)

    # Move turtle to the next line
    pen.penup()
    pen.goto(-300, 0)
    pen.pendown()

    # Drawing "SO MUCH"
    for letter in "SO MUCH":
        draw_letter(letter)

# Call the function to draw the message
draw_message()

# Hide turtle after writing
pen.hideturtle()

# Keep the window open until closed by the user
turtle.done()
