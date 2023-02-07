def rectangle(length, width):
    if type(length) != int or type(width) != int:
        return "Enter valid values!"

    def area(length, width):
        return length * width

    def perimeter(length, width):
        return 2 * length + 2 * width

    return f'Rectangle area: {area(length, width)}\nRectangle perimeter: {perimeter(length, width)}'


print(rectangle(2, 10))
print(rectangle('2', 10))


