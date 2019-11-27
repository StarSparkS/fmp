from decimal import *
def D2Hfx(start_date, end_date, percentage):
    return Decimal(start_date + end_date * percentage)
def AM(*args):
    print("Hello")
    for arg in args:
        print(arg)