class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_perimetr(self):
        return 2 * (self.w + self.h)


# print(__name__)  # rect.py - __main__

# Запуск со start.py - geometry.rect

# __author__ = "Elena"
# if __name__ == '__main__':
#     print(__author__)

if __name__ == '__main__':
    r1 = Rectangle(10, 20)
    print("Class Rectangle", r1.get_perimetr())
