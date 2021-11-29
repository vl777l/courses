import turtle
import pyautogui


class Rectangle:
    def rec(self):
        wn = turtle.Screen()
        alex = turtle.Turtle()
        wn.bgcolor("white")
        alex.color("black")
        alex.begin_fill()
        for n in range(2):
            alex.forward(100)
            alex.right(90)
            alex.forward(50)
            alex.right(90)
        alex.end_fill()
        alex.color("white")
        #wn.exitonclick()


class MousePress:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def press(self, x, y):
        pyautogui.moveTo(x, y, duration=1)
        pyautogui.click()


class Button(Rectangle, MousePress):
    def press_button(self):
        parent_class_object = super()
        graph = parent_class_object.rec()
        pre = parent_class_object.press(x, y)
        return graph and pre


x = int(input("Координаты кнопки x: "))
y = int(input("Координаты кнопки y: "))
my_rectangle = Rectangle()
my_rectangle.rec()
my_button = Button(x, y)
my_button.press_button()
