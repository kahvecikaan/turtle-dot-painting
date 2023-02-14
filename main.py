# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 10)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
# To extract the color palette of the desired picture

import turtle as t
import random

t.colormode(255)

color_list = [(222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (239, 230, 223), (126, 40, 61), (21, 86, 61),
              (59, 48, 37),
              (250, 194, 42), (13, 117, 146), (57, 146, 72), (229, 86, 36), (231, 172, 190), (57, 71, 39),
              (197, 102, 134),
              (197, 125, 150), (156, 191, 185), (30, 67, 58), (236, 245, 241), (166, 204, 202)]

tim = t.Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fast")
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

num_of_dots = 100
for dot_count in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()
