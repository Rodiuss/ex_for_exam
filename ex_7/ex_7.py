from tkinter import ttk, Tk, IntVar, W


root = Tk()
root.geometry('500x400')
root.title('program')

my_var = IntVar()
my_var.set(0)

first = ttk.Radiobutton(root,
                        text='Треугольник',
                        variable=my_var,
                        value=0).grid(column=1, row=1, sticky=W, padx=20)
second = ttk.Radiobutton(root,
                         text='Параллеограмм',
                         variable=my_var,
                         value=1).grid(column=1, row=2, sticky=W, padx=20)
third = ttk.Radiobutton(root,
                        text='Ромб',
                        variable=my_var,
                        value=2).grid(column=1, row=3, sticky=W, padx=20)
fourth = ttk.Radiobutton(root,
                         text='Прямоугольник',
                         variable=my_var,
                         value=3).grid(column=2, row=1, sticky=W, padx=20)
fifth = ttk.Radiobutton(root,
                        text='квадрат',
                        variable=my_var,
                        value=4).grid(column=2, row=2, sticky=W, padx=20)
sixth = ttk.Radiobutton(root,
                        text='трапеция',
                        variable=my_var,
                        value=5).grid(column=2, row=3, sticky=W, padx=20)
seventh = ttk.Radiobutton(root,
                          text='круг',
                          variable=my_var,
                          value=6).grid(column=1, row=4, sticky=W, padx=20)
label = ttk.Label(root, text='Число 1').grid(column=1, row=5)
e_first = ttk.Entry(root).grid(column=2, row=5)
label = ttk.Label(root, text='Число 2').grid(column=1, row=6)
e_second = ttk.Entry(root).grid(column=2, row=6)
label = ttk.Label(root, text='Число 3').grid(column=1, row=7)
e_third = ttk.Entry(root).grid(column=2, row=7)
label = ttk.Label(root, text='Число 4').grid(column=1, row=8)
e_fourth = ttk.Entry(root).grid(column=2, row=8)
label = ttk.Label(root, text='Число 5').grid(column=1, row=9)
e_fifth = ttk.Entry(root).grid(column=2, row=9)
label = ttk.Label(root, text='Число 6').grid(column=1, row=10)
e_sixth = ttk.Entry(root).grid(column=2, row=10)
label = ttk.Label(root, text='Число 7').grid(column=1, row=11)
e_seventh = ttk.Entry(root).grid(column=2, row=11)


def calc(func):
    pass


root.mainloop()


'''Какую операцию вы хотите выполнить?
\n 1 периметр треугольника
\n 2 периметр параллелограмма
\n 3 периметр ромба
\n 4 периметр прямоугольника
\n 5 периметр квадрата
\n 6 периметр трапеции
\n 7 периметр круга
\n'))

if v == 1:
    q1 = int(input('Введите число 1: '))
    q2 = int(input('Введите число 2: '))
    q3 = int(input('Введите число 3: '))
    r = q1 + q2 + q3
    p = 'периметр'
    t = p
if v == 2:
    q1 = int(input('Введите число 1: '))
    q2 = int(input('Введите число 2: '))
    q3 = int(input('Введите число 3: '))
    q4 = int(input('Введите число 4: '))
    r = q1 + q2 + q3 + q4
    l = 'периметр'
    t = l
if v == 3:
    q1 = int(input('Введите число 1: '))
    r = 4 * q1
    m = 'периметр'
    t = m
if v == 4:
    q1 = int(input('Введите число 1: '))
    q2 = int(input('Введите число 2: '))
    r = 2*q1 + 2*q2
    n = 'периметр'
    t = n
if v == 5:
    q1 = int(input('Введите число 1: '))
    r = 4*q1
    k = 'периметр'
    t = k
if v == 6:
    q1 = int(input('Введите число 1: '))
    q2 = int(input('Введите число 2: '))
    q3 = int(input('Введите число 3: '))
    q4 = int(input('Введите число 4: '))
    r = q1 + q2 + q3 + q4
    b = 'периметр'
    t = b
if v == 7:
    q1 = int(input('Введите число 1: '))
    r = 3.14 * q1
    c = 'периметр'
    t = c
print('Результат ', t, ' = ', r)'''
