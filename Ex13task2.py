class English:
    def greeting(self):
        return "Hello everyone.\n We hope you ready to start learn somthing interest"


class Spanish:
    def greeting(self):
        return "Hola, todos.\n Esperamos que estés listo para comenzar a aprender algo de interés."


def hello_friend():
    return mark.greeting()+"\n\n"+ann.greeting()


mark = English()
ann = Spanish()
print(hello_friend())