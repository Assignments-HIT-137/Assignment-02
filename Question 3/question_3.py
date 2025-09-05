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
        
        #For each third of the length the turtle turns 60 degree right then 120 degree left and 60 degree right again and if the depth is zero, it moves straight for remaining length.
        draw_edge(length, depth - 1)
        turtle.right(60)
        draw_edge(length, depth - 1)
        turtle.left(120)
        draw_edge(length, depth - 1)
        turtle.right(60)
        draw_edge(length, depth - 1)
        
        

def draw_polygon(sides, side_length, depth):
    angle = 360 / sides
    for _ in range(sides):
        draw_edge(side_length, depth)
        turtle.right(angle)

def main():
    # Ask user for input and check if only integer is entered or not
    try:

        sides = int(input("Enter number of sides: "))
        side_length = float(input("Enter side length (in pixels): "))
        depth = int(input("Enter recursion depth: "))
    except:
        print("Please enter a valid number")
        exit()        

    # Setup turtle
    turtle.speed(0) 
    
    
   #Set the background and pen color  
    turtle.bgcolor("white")
    turtle.pencolor("black")

    
    
    draw_polygon(sides, side_length, depth)

    # Finish
    turtle.done()







if __name__ == "__main__":
    main()