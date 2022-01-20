class Circle:
    def area(self):
        print("2*22/7*radius")


class Rectangle(Circle):
    def area(self):
        print("Length*breadth")


if __name__ == "__main__":
    rectangle = Rectangle()
    rectangle.area()
