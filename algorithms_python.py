from math import sin, pi
import turtle

# Setup
t = turtle.Turtle()
wn = turtle.Screen()
wn.setup(width=800, height=800)
wn.bgcolor("black")
t.shape("turtle")
t.speed(0)
t.hideturtle()

# Expanded color palette
colors = [
    "red", "deep pink", "hot pink", "light pink",
    "purple", "magenta", "violet", "orchid",
    "dodger blue", "deep sky blue", "cyan", "aqua"
]

def color(iteration):
    """Set pen color based on iteration"""
    t.pencolor(colors[iteration % len(colors)])

def at(x, y):
    """Move turtle to position without drawing"""
    t.penup()
    t.home()
    t.goto(x, y)
    t.pendown()

def heart(size, shape):
    """Draw a mathematical heart shape"""
    t.pensize(3)
    radius = size * sin(shape * pi / 180) / (1 + sin((90 - shape) * pi / 180))
    t.right(shape)
    t.forward(size)
    t.circle(radius, 180 + shape)
    t.right(180)
    t.circle(radius, 180 + shape)
    t.forward(size)
    t.left(180 - shape)

def filled_heart(size, shape, fill_color):
    """Draw a filled heart"""
    t.fillcolor(fill_color)
    t.begin_fill()
    heart(size, shape)
    t.end_fill()

def draw_spiral_hearts():
    """Draw hearts in a spiral pattern"""
    turtle.delay(0)
    angle = 0
    for iteration in range(1, 20):
        color(iteration)
        x = iteration * 8 * sin(angle * pi / 180)
        y = iteration * 8 * sin(angle * pi / 180) - 50
        at(x, y)
        t.right(angle)
        heart(iteration * 5, 45)
        t.left(angle)
        angle += 360 / 19

def draw_circle_hearts():
    """Draw hearts arranged in a circle"""
    turtle.delay(0)
    radius = 150
    num_hearts = 12
    for i in range(num_hearts):
        angle = (360 / num_hearts) * i
        x = radius * sin(angle * pi / 180)
        y = radius * sin((angle + 90) * pi / 180)
        
        color(i)
        at(x, y)
        t.setheading(angle + 90)
        filled_heart(20, 45, colors[i % len(colors)])
        t.setheading(0)

def draw_cascading_hearts():
    """Draw hearts cascading down with varying sizes"""
    turtle.delay(0)
    for iteration in range(1, 16):
        color(iteration)
        at(0, 200 - iteration * 25)
        heart(iteration * 6, 45)

def draw_expanding_hearts():
    """Draw hearts expanding from center"""
    turtle.delay(0)
    for iteration in range(1, 14):
        color(iteration)
        at(0, iteration * -5)
        heart(iteration * 10, 45)

def write_message(text, x, y, size=14, text_color="red"):
    """Write text on screen"""
    t.penup()
    t.goto(x, y)
    t.color(text_color)
    t.write(text, align="center", font=("Arial", size, "bold"))

# Main Animation
def main():
    # Title
    write_message("Valentine's Day Special", 0, 300, 20, "hot pink")
    
    # Choose your animation style (uncomment one):
    
    # Style 1: Expanding hearts (original style)
    draw_expanding_hearts()
    
    # Style 2: Spiral hearts (uncomment to use)
    # draw_spiral_hearts()
    
    # Style 3: Circle of hearts (uncomment to use)
    # draw_circle_hearts()
    
    # Style 4: Cascading hearts (uncomment to use)
    # draw_cascading_hearts()
    
    # Romantic poem
    write_message("Roses are red", 0, -180, 16, "deep pink")
    write_message("Violets are blue", 0, -210, 16, "dodger blue")
    write_message("I love coding", 0, -240, 16, "magenta")
    write_message("And I love you!", 0, -270, 16, "red")
    
    # Signature
    write_message("Made with Python & Love", 0, -320, 10, "light pink")
    
    t.goto(0, -350)
    wn.update()

# Run the animation
if __name__ == "__main__":
    main()
    turtle.done()