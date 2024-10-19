import math

class Polygon:
    def area(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

def main():
    # Create instances of each polygon
    triangle = Triangle(10, 5)
    rectangle = Rectangle(4, 6)
    circle = Circle(3)

    # Calculate and print the area of each polygon
    print(f"Area of Triangle: {triangle.area()}")
    print(f"Area of Rectangle: {rectangle.area()}")
    print(f"Area of Circle: {circle.area()}")

if __name__ == "__main__":
    main()
