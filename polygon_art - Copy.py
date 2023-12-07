import turtle
import random

class Shapemaster:
    def __init__(self):


def draw_polygon(num_sides, size, orientation, location, color, border_size):
    turtle.penup()
    turtle.goto(location[0], location[1])
    turtle.setheading(orientation)
    turtle.color(color)
    turtle.pensize(border_size)
    turtle.pendown()
    for _ in range(num_sides):
        turtle.forward(size)
        turtle.left(360/num_sides)
    turtle.penup()


def get_new_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)


##########

num_shapes = 25 #random.randint(20, 30)

rand_sizes = []
rand_orientations = []
rand_locations = []
rand_colors = []
rand_b_size = []
for i in range(num_shapes):
    rand_sizes.append(random.randint(50, 150))
    rand_orientations.append(random.randint(0, 90))
    rand_locations.append([random.randint(-300, 300), random.randint(-200, 200)])
    rand_colors.append(get_new_color())
    rand_b_size.append(random.randint(1, 10))

choice = 0
reduction_ratio = 0.618
while not 1 <= choice <= 8:
    choice = int(input('Which art do you want to generate? Enter a number between 1 to 8, inclusive: '))
if choice == 1:
    num_sides = 3
    for i in range(num_shapes):
        size = rand_sizes[i]
        orientation = rand_orientations[i]
        location = rand_locations[i]
        color = rand_colors[i]
        border_size = rand_b_size[i]
        draw_polygon(num_sides, size, orientation, location, color, border_size)

elif choice == 2:
    num_sides = 4
    for i in range(num_shapes):
        size = rand_sizes[i]
        orientation = rand_orientations[i]
        location = rand_locations[i]
        color = rand_colors[i]
        border_size = rand_b_size[i]
        draw_polygon(num_sides, size, orientation, location, color, border_size)

elif choice == 3:
    num_sides = 5
    for i in range(num_shapes):
        size = rand_sizes[i]
        orientation = rand_orientations[i]
        location = rand_locations[i]
        color = rand_colors[i]
        border_size = rand_b_size[i]
        draw_polygon(num_sides, size, orientation, location, color, border_size)

elif choice == 4:
    for i in range(num_shapes):
        num_sides = random.randint(3, 5)
        size = rand_sizes[i]
        orientation = rand_orientations[i]
        location = rand_locations[i]
        color = rand_colors[i]
        border_size = rand_b_size[i]
        draw_polygon(num_sides, size, orientation, location, color, border_size)

elif choice == 5:
    num_sides = 3
    for i in range(num_shapes):
        size = rand_sizes[i]
        orientation = rand_orientations[i]
        location = rand_locations[i]
        color = rand_colors[i]
        border_size = rand_b_size[i]
        for j in range(4):
            draw_polygon(num_sides, size, orientation, location, color, border_size)
            turtle.penup()
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.right(90)
            location[0] = turtle.pos()[0]
            location[1] = turtle.pos()[1]
            size *= reduction_ratio

elif choice == 6:
    num_sides = 4
    for i in range(num_shapes):
        size = rand_sizes[i]
        orientation = rand_orientations[i]
        location = rand_locations[i]
        color = rand_colors[i]
        border_size = rand_b_size[i]
        for j in range(4):
            draw_polygon(num_sides, size, orientation, location, color, border_size)
            turtle.penup()
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.right(90)
            location[0] = turtle.pos()[0]
            location[1] = turtle.pos()[1]
            size *= reduction_ratio

elif choice == 7:
    num_sides = 5
    for i in range(num_shapes):
        size = rand_sizes[i]
        orientation = rand_orientations[i]
        location = rand_locations[i]
        color = rand_colors[i]
        border_size = rand_b_size[i]
        for j in range(4):
            draw_polygon(num_sides, size, orientation, location, color, border_size)
            turtle.penup()
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.right(90)
            location[0] = turtle.pos()[0]
            location[1] = turtle.pos()[1]
            size *= reduction_ratio

elif choice == 8:
    for i in range(num_shapes):
        num_sides = random.randint(3, 5)
        size = rand_sizes[i]
        orientation = rand_orientations[i]
        location = rand_locations[i]
        color = rand_colors[i]
        border_size = rand_b_size[i]
        for j in range(4):
            draw_polygon(num_sides, size, orientation, location, color, border_size)
            turtle.penup()
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.right(90)
            location[0] = turtle.pos()[0]
            location[1] = turtle.pos()[1]
            size *= reduction_ratio

# # reposition the turtle and get a new location
# for i in range(10):
#     turtle.penup()
#     turtle.forward(size*(1-reduction_ratio)/2)
#     turtle.left(90)
#     turtle.forward(size*(1-reduction_ratio)/2)
#     turtle.right(90)
#     location[0] = turtle.pos()[0]
#     location[1] = turtle.pos()[1]
#
#     # adjust the size according to the reduction ratio
#     size *= reduction_ratio
#
#     # draw the second polygon embedded inside the original
#     draw_polygon(num_sides, size, orientation, location, color, border_size)


    # size = random.randint(50, 150)
    # orientation = random.randint(0, 90)
    # location = [random.randint(-300, 300), random.randint(-200, 200)]
    # color = get_new_color()
    # border_size = random.randint(1, 10)
    #
    # draw_polygon(num_sides, size, orientation, location, color, border_size)


#
# # draw a polygon at a random location, orientation, color, and border line thickness
# num_sides = random.randint(3, 5) # triangle, square, or pentagon
# size = random.randint(50, 150)
# orientation = random.randint(0, 90)
# location = [random.randint(-300, 300), random.randint(-200, 200)]
# color = get_new_color()
# border_size = random.randint(1, 10)
# draw_polygon(num_sides, size, orientation, location, color, border_size)
#
#


# hold the window; close it by clicking the window close 'x' mark
turtle.done()