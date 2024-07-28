from turtle import *

# Set up the screen
setup(1200, 600)
speed(0)  # Set the drawing speed to the fastest

# Move the turtle to the starting position
up()
goto(-600, 0)
down()

# Loop to draw 8 patterns
for i in range(8):
    # Draw a blue square
    color('blue')
    for _ in range(4):
        forward(50)
        right(90)
    
    # Move forward a bit
    color('black')
    forward(20)
    
    # Draw a red triangle
    color('red')
    for _ in range(3):
        forward(50)
        right(120)
    
    # Move forward to start the next pattern
    color('black')
    forward(70)

# Wait for the user to press Enter to exit
input("Presser entrée pour quitter")
