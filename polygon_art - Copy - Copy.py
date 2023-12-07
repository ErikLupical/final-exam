import turtle
import random

turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)


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
            turtle.forward(size)
            turtle.left(360/num_sides)
        turtle.penup()

def get_new_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

class Session:
    def __init__(self, shape):
        self.shape = shape

    def gen_rands(self):
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
        return rand_sizes, rand_orientations, rand_locations, rand_colors, rand_b_size

    def make_art_1(self, num_shapes):
        for i in range(num_shapes):
            size = self.shape.size = self.gen_rands()[0]
            orientation = self.shape.orientation = self.gen_rands()[1]
            location = self.shape.location = self.gen_rands()[2]
            color = self.shape.color = self.gen_rands()[3]
            border_size = self.shape.size = self.gen_rands()[4]
            self.shape.draw_polygon(self.shape.num_sides, size, orientation, location, color, border_size)

    def make_art_1_1(self, num_shapes):
        for i in range(num_shapes):
            num_sides = random.randint(3, 5)
            size = self.shape.size = self.gen_rands()[0]
            orientation = self.shape.orientation = self.gen_rands()[1]
            location = self.shape.location = self.gen_rands()[2]
            color = self.shape.color = self.gen_rands()[3]
            border_size = self.shape.size = self.gen_rands()[4]
            self.shape.draw_polygon(num_sides, size, orientation, location, color, border_size)


    def make_art_2(self, num_shapes):
        for i in range(num_shapes):
            size = self.shape.size = self.gen_rands()[0]
            orientation = self.shape.orientation = self.gen_rands()[1]
            location = self.shape.location = self.gen_rands()[2]
            color = self.shape.color = self.gen_rands()[3]
            border_size = self.shape.size = self.gen_rands()[4]
            for _ in range(4):
                self.shape.draw_polygon(self.shape.num_sides, size, orientation, location, color, border_size)
                turtle.penup()
                turtle.forward(size * (1 - reduction_ratio) / 2)
                turtle.left(90)
                turtle.forward(size * (1 - reduction_ratio) / 2)
                turtle.right(90)
                location[0] = turtle.pos()[0]
                location[1] = turtle.pos()[1]
                size *= reduction_ratio

    def make_art_2_1(self, num_shapes):
        for i in range(num_shapes):
            num_sides = random.randint(3, 5)
            size = self.shape.size = self.gen_rands()[0]
            orientation = self.shape.orientation = self.gen_rands()[1]
            location = self.shape.location = self.gen_rands()[2]
            color = self.shape.color = self.gen_rands()[3]
            border_size = self.shape.size = self.gen_rands()[4]
            for _ in range(4):
                self.shape.draw_polygon(num_sides, size, orientation, location, color, border_size)
                turtle.penup()
                turtle.forward(size * (1 - reduction_ratio) / 2)
                turtle.left(90)
                turtle.forward(size * (1 - reduction_ratio) / 2)
                turtle.right(90)
                location[0] = turtle.pos()[0]
                location[1] = turtle.pos()[1]
                size *= reduction_ratio


##########


num_shapes = random.randint(20, 30)

choice = 0
reduction_ratio = 0.618

while not 1 <= choice <= 8:
    choice = int(input('Which art do you want to generate? Enter a number between 1 to 8, inclusive: '))

size = 0
orientation = 0
location = []
color = []
border_size = 0

if 1 <= choice <= 3:
    if choice == 1:
        num_sides = 3
    elif choice == 2:
        num_sides = 4
    elif choice == 3:
        num_sides = 5

    shape = Shape(num_sides, size, orientation, location, color, border_size)
    session = Session(shape)
    session.make_art_1(num_shapes)

    if choice == 4:
        shape = Shape(0, size, orientation, location, color, border_size)
        session = Session(shape)
        session.make_art_1_1(num_shapes)

if 5 <= choice <= 7:
    if choice == 5:
        num_sides = 3
    elif choice == 6:
        num_sides = 4
    elif choice == 7:
        num_sides = 5

    shape = Shape(num_sides, size, orientation, location, color, border_size)
    session = Session(shape)
    session.make_art_2(num_shapes)

elif choice == 8:
    shape = Shape(0, size, orientation, location, color, border_size)
    session = Session(shape)
    session.make_art_2_1(num_shapes)

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