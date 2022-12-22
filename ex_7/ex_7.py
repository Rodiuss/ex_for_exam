from tkinter import *
import os


def formula():
    try:
        if label5.cget("text") == "Треугольник":
            if float(entry1.get()) <= 0 or float(entry2.get()) <= 0:
                itog = "Введите число больше нуля!"
            else:
                itog = float(entry1.get()) * float(entry2.get()) / 2
        elif label5.cget("text") == "Параллелограмм":
            if float(entry1.get()) <= 0 or float(entry2.get()) <= 0:
                itog = "Введите число больше нуля!"
            else:
                itog = float(entry1.get()) * float(entry2.get())
        elif label5.cget("text") == "Ромб":
            if float(entry1.get()) <= 0 or float(entry2.get()) <= 0:
                itog = "Введите число больше нуля!"
            else:
                itog = float(entry1.get()) * float(entry2.get())
        elif label5.cget("text") == "Прямоугольник":
            if float(entry1.get()) <= 0 or float(entry2.get()) <= 0:
                itog = "Введите число больше нуля!"
            else:
                itog = float(entry1.get()) * float(entry2.get())
        elif label5.cget("text") == "Квадрат":
            if float(entry1.get()) <= 0:
                itog = "Введите число больше нуля!"
            else:
                itog = float(entry1.get()) * float(entry1.get())
        elif label5.cget("text") == "Трапеция":
            if float(entry1.get()) <= 0 or float(entry2.get()) <= 0 or float(entry4.get()) <= 0:
                itog = "Введите число больше нуля!"
            else:
                itog = float(entry1.get()) * float(entry2.get()) * \
                    float(entry4.get()) / 2
        elif label5.cget("text") == "Круг":
            if float(entry1.get()) <= 0:
                itog = "Введите число больше нуля!"
            else:
                itog = float(entry1.get()) * float(entry1.get()) * 3.14

        entry3.delete(0, 'end')
        entry3.insert(0, str(itog))

    except ValueError:
        entry3.delete(0, 'end')
        entry3.insert(0, str("Введите число!"))


def triangle():
    label5.config(text="Треугольник")
    label1.config(text="Введите b:")
    label2.config(text="Введите h:")
    label2.place(x=5, y=45)
    entry2.place(x=5, y=65)
    label3.place(x=5, y=85)
    entry3.place(x=5, y=105)
    label6.place(x=-150, y=-100)
    entry4.place(x=-150, y=-100)
    button1.place(x=5, y=130)
    button2.place(x=5, y=160)


def parallelogram():
    label5.config(text="Параллелограмм")
    label1.config(text="Введите b:")
    label2.config(text="Введите h:")
    label2.place(x=5, y=45)
    entry2.place(x=5, y=65)
    label3.place(x=5, y=85)
    entry3.place(x=5, y=105)
    label6.place(x=-100, y=125)
    entry4.place(x=-100, y=-100)
    button1.place(x=5, y=130)
    button2.place(x=5, y=160)


def rhomb():
    label5.config(text="Ромб")
    label1.config(text="Введите b:")
    label2.config(text="Введите h:")
    label2.place(x=5, y=45)
    entry2.place(x=5, y=65)
    label3.place(x=5, y=85)
    entry3.place(x=5, y=105)
    label6.place(x=-100, y=125)
    entry4.place(x=-100, y=-100)
    button1.place(x=5, y=130)
    button2.place(x=5, y=160)


def rectangle():
    label5.config(text="Прямоугольник")
    label1.config(text="Введите L:")
    label2.config(text="Введите w:")
    label2.place(x=5, y=45)
    entry2.place(x=5, y=65)
    label3.place(x=5, y=85)
    entry3.place(x=5, y=105)
    label6.place(x=-100, y=125)
    entry4.place(x=-100, y=-100)
    button1.place(x=5, y=130)
    button2.place(x=5, y=160)


def square():
    label5.config(text="Квадрат")
    label1.config(text="Введите l:")
    label2.place(x=-100, y=-45)
    entry2.place(x=-100, y=-65)
    label3.place(x=5, y=45)
    entry3.place(x=5, y=65)
    label6.place(x=-100, y=-125)
    entry4.place(x=-100, y=-100)
    button1.place(x=5, y=95)
    button2.place(x=5, y=125)


def trapezoid():
    label5.config(text="Трапеция")
    label1.config(text="Введите b:")
    label2.config(text="Введите h:")
    label2.place(x=5, y=45)
    entry2.place(x=5, y=65)
    label3.place(x=5, y=125)
    entry3.place(x=5, y=145)
    label6.place(x=5, y=85)
    entry4.place(x=5, y=105)
    button1.place(x=5, y=175)
    button2.place(x=5, y=205)


def tircle():
    label5.config(text="Круг")
    label1.config(text="Введите r:")
    label2.place(x=-100, y=-45)
    entry2.place(x=-100, y=-65)
    label3.place(x=5, y=45)
    entry3.place(x=5, y=65)
    label6.place(x=-100, y=125)
    entry4.place(x=-100, y=-100)
    button1.place(x=5, y=95)
    button2.place(x=5, y=125)


def description():
    os.startfile(r'photo.png')


root = Tk()
root.title("Вычисление площадей")
root.geometry("440x250")
root.resizable(width=False, height=False)
label1 = Label(root, text="Введите b:")
label1.place(x=5, y=5)
entry1 = Entry(root, width=50)
entry1.place(x=5, y=25)
label2 = Label(root, text="Введите h:")
label2.place(x=5, y=45)
entry2 = Entry(root, width=50)
entry2.place(x=5, y=65)
label3 = Label(root, text="Ответ:")
label3.place(x=5, y=85)
entry3 = Entry(root, width=50)
entry3.place(x=5, y=105)
label6 = Label(root, text="Введите B:")
label6.place(x=-100, y=85)
entry4 = Entry(root, width=50)
entry4.place(x=-100, y=-100)
button1 = Button(root, text="Вычислить", width=12, command=formula)
button1.place(x=5, y=130)
button2 = Button(root, text="Описание фигур", width=12, command=description)
button2.place(x=5, y=160)
label4 = Label(root, text="Выбрана  фигура:")
label4.place(x=200, y=190)
label5 = Label(root, text="Треугольник")
label5.place(x=310, y=190)
mainmenu = Menu(root)
root.config(menu=mainmenu)
vidmenu = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="Выберите фигуру", menu=vidmenu)
vidmenu.add_command(label="Треугольник", command=triangle)
vidmenu.add_command(label="Параллелограмм", command=parallelogram)
vidmenu.add_command(label="Ромб", command=rhomb)
vidmenu.add_command(label="Прямоугольник", command=rectangle)
vidmenu.add_command(label="Квадрат", command=square)
vidmenu.add_command(label="Трапеция", command=trapezoid)
vidmenu.add_command(label="Круг", command=tircle)
root.mainloop()
