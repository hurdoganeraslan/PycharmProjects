import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("green")
drawing_board.title("Python Turtle")


'''
turtle_instance = turtle.Turtle()
turtle_instance.forward(108)
turtle_instance_2 = turtle.Turtle()
turtle_instance_2.left(180)
turtle_instance_2.forward(100)
turtle.done()
'''

#square
'''

turtle_instance = turtle.Turtle()
for i in range(4):
    turtle_instance.forward(200)
    turtle_instance.left(90)
'''
#star

''''
turtle_instance = turtle.Turtle()
for i in range(5):
    turtle_instance.right(144)
    turtle_instance.forward(300)
    
    turtle.done()
'''
#poligon

turtle_instance = turtle.Turtle()
num_sides=8
angle = 360.0 / num_sides
side_length = 100

for i in range(num_sides):
    turtle_instance.right(angle)
    turtle_instance.forward(side_length)

turtle.done()




