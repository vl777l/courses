class Editor:
    def view_document(self, fil):
        f = open(fil, "r")
        cont = f.readlines()
        return print(cont)

    def edit_document(self, fil):
        return print("Редактирование документов недоступно для бесплатной версии")


class ProEditor(Editor):
    def edit_document(self, fil):
        f = open(fil, "w")
        f.write(input())
        f.close()


fi = "fil.txt"
print("Введите с клавиатуры лицензионный ключ")
key = str(input("Поле для ключа: "))
if len(key) >= 8:
    fil = ProEditor()
    fil.edit_document(fi)
    #fil.view_document(fi)
else:
    fil = Editor()
   #fil.view_document(fi)
    fil.edit_document(fi)