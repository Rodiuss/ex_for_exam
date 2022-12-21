from math import ceil


def calc(lino, room):
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

    all_price = unit_price * ceil(room / square)
    print(all_price)


my_calc = calc(lino=3, room=199)
