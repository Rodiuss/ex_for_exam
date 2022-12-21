from tkinter.messagebox import showerror
from math import ceil


def calc(room, lino=0):
    # англ
    room = room.replace(' ', '')
    room = room.replace('x', ' ')
    room = room.replace('X', ' ')
    # рус
    room = room.replace('х', ' ')
    room = room.replace('Х', ' ')

    room = room.replace(',', '.')
    room = room.split(' ')

    try:
        a, b = float(room[0]), float(room[1])
    except Exception:
        showerror(message='Ты лох')
        return False

    square = None
    unit_price = None

    match lino:
        case 0:
            square = 1.5
            unit_price = 357
        case 1:
            square = 3
            unit_price = 750
        case 2:
            square = 2.5
            unit_price = 632
        case 3:
            square = 4.5
            unit_price = 950

    count = ceil(a * b / square)
    all_price = count * unit_price
    print(f'{count} рулонов обойдутся в {all_price} рублей')


my_calc = calc(lino=3, room='6 x 4,5')
