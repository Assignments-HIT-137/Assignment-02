import turtle

def draw_edge(length, depth):
    """
    Recursively draw one edge with indentation pattern.
    If depth=0, just draw a straight line.
    """
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 3
        draw_edge(length, depth - 1)
        turtle.right(60)
        draw_edge(length, depth - 1)
        turtle.left(120)
        draw_edge(length, depth - 1)
        turtle.right(60)
        draw_edge(length, depth - 1)
        
        

def draw_polygon(sides, side_length, depth):
    """
    Draw a polygon with recursive patterned edges.
    """
    angle = 360 / sides
    for _ in range(sides):
        draw_edge(side_length, depth)
        turtle.right(angle)

def main():
    # Ask user for input
    try:

        sides = int(input("Enter number of sides: "))
        side_length = float(input("Enter side length (in pixels): "))
        depth = int(input("Enter recursion depth: "))
    except:
        print("Please enter a valid number")
        exit()        

    # Setup turtle
    turtle.speed(0)  # fastest
    turtle.hideturtle()
    turtle.bgcolor("white")
    turtle.pencolor("black")

    # Move to starting position
    turtle.penup()
    turtle.goto(-side_length/2, -side_length/2)
    turtle.pendown()
    #Draw Pattern
    draw_polygon(sides, side_length, depth)

    # Finish
    turtle.done()







if __name__ == "__main__":
    main()