import turtle
import random

class Shape:
    def __init__(self, num_sides, size, orientation, location, color, border_size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size

    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        turtle.penup()


def get_new_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


##########


turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

num_shapes = 25  # random.randint(20, 30)

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
    for i in range(num_shapes):
        shape = Shape(3, rand_sizes[i], rand_orientations[i], rand_locations[i], rand_colors[i], rand_b_size[i])
        shape.draw_polygon()

elif choice == 2:
    for i in range(num_shapes):
        shape = Shape(4, rand_sizes[i], rand_orientations[i], rand_locations[i], rand_colors[i], rand_b_size[i])
        shape.draw_polygon()

elif choice == 3:
    for i in range(num_shapes):
        for i in range(num_shapes):
            shape = Shape(5, rand_sizes[i], rand_orientations[i], rand_locations[i], rand_colors[i], rand_b_size[i])
            shape.draw_polygon()

elif choice == 4:
    for i in range(num_shapes):
        shape = Shape(random.randint(3, 5), rand_sizes[i], rand_orientations[i], rand_locations[i], rand_colors[i], rand_b_size[i])
        shape.draw_polygon()

elif choice == 5:
    for i in range(num_shapes):
        shape = Shape(3, rand_sizes[i], rand_orientations[i], rand_locations[i], rand_colors[i], rand_b_size[i])
        for _ in range(4):
            shape.draw_polygon()
            turtle.penup()
            turtle.forward(shape.size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(shape.size*(1-reduction_ratio)/2)
            turtle.right(90)
            shape.location[0] = turtle.pos()[0]
            shape.location[1] = turtle.pos()[1]
            shape.size *= reduction_ratio

elif choice == 6:
    for i in range(num_shapes):
        shape = Shape(4, rand_sizes[i], rand_orientations[i], rand_locations[i], rand_colors[i], rand_b_size[i])
        for _ in range(4):
            shape.draw_polygon()
            turtle.penup()
            turtle.forward(shape.size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(shape.size*(1-reduction_ratio)/2)
            turtle.right(90)
            shape.location[0] = turtle.pos()[0]
            shape.location[1] = turtle.pos()[1]
            shape.size *= reduction_ratio

elif choice == 7:
    for i in range(num_shapes):
        shape = Shape(5, rand_sizes[i], rand_orientations[i], rand_locations[i], rand_colors[i], rand_b_size[i])
        for _ in range(4):
            shape.draw_polygon()
            turtle.penup()
            turtle.forward(shape.size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(shape.size*(1-reduction_ratio)/2)
            turtle.right(90)
            shape.location[0] = turtle.pos()[0]
            shape.location[1] = turtle.pos()[1]
            shape.size *= reduction_ratio

elif choice == 8:
    for i in range(num_shapes):
        shape = Shape(random.randint(3,5), rand_sizes[i], rand_orientations[i], rand_locations[i], rand_colors[i], rand_b_size[i])
        for _ in range(4):
            shape.draw_polygon()
            turtle.penup()
            turtle.forward(shape.size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(shape.size*(1-reduction_ratio)/2)
            turtle.right(90)
            shape.location[0] = turtle.pos()[0]
            shape.location[1] = turtle.pos()[1]
            shape.size *= reduction_ratio


# hold the window; close it by clicking the window close 'x' mark
turtle.done()
