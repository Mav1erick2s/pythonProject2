from rectangle_1 import Rectangle, Square, Circle

rect1 = Rectangle(3,4)
rect2 = Rectangle(5,6)

print(rect1.get_area())
print(rect2.get_area())



square_1 = Square(10)
square_2 = Square(11)

print(square_1.get_area_square())
print(square_2.get_area_square())



circle_1 = Circle(4)
circle_2 = Circle(6)

print(circle_1.get_area_circle())
print(circle_2.get_area_circle())



figures = [rect1, rect2, square_1, square_2, circle_1, circle_2]

for figure in figures:
    if isinstance(figure,Square):
        print(figure.get_area_square())
    elif isinstance(figure, Circle):
        print(figure.get_area_circle())
    else:
        print(figure.get_area())

