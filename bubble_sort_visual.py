from os import system
from time import sleep
from random import randint

A = lambda s: sleep(s)
M = lambda s: input()


def clrscr():
    system('cls')
    print("----------------------------------------------------")
    print("|            Bubble sort Visualization             |")
    print("----------------------------------------------------")


# class of colors for background and font
class colors:
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'

    class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'

    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        light = '\033[47m'


def print_swap(i_index, j_index, _list):
    toggle_color = [colors.bg.red, colors.bg.light]

    for _ in range(2):
        clrscr()
        for index in range(len(_list)):
            if index == j_index:
                print(toggle_color[_ % 2], colors.fg.blue, _list[index], end=" ")
            elif index == i_index:
                print(toggle_color[((_ % 2) * (-1)) + 1], colors.fg.blue, _list[index], end=" ")
            else:
                print(colors.bg.black, colors.fg.lightgrey, _list[index], end=" ")
        print()
        print(colors.bg.black, colors.fg.cyan, f"Swapping :{_list[i_index]} <-> {_list[j_index]} ", end=" ")
        print(colors.bg.black, colors.fg.lightgrey)
        delay(0.5)
        _list[i_index], _list[j_index] = _list[j_index], _list[
            i_index]  # just to display actual list will be sorted in sort() function


def print_list(i_index, j_index, _list):
    print(colors.bold)
    clrscr()
    for _ in range(len(_list)):
        if _ == j_index:
            print(colors.bg.orange, colors.fg.blue, _list[_], end=" ")
        elif _ == i_index:
            print(colors.bg.purple, colors.fg.blue, _list[_], end=" ")
        else:
            print(colors.bg.black, colors.fg.lightgrey, _list[_], end=" ")
    print(colors.bg.black, colors.fg.lightgrey)


def sort(values):
    for i in range(0, len(values) - 1):
        for j in range(i + 1, len(values)):
            if values[j] < values[i]:
                print_list(i, j, values)
                delay(3)
                print_swap(i, j, values)
                if delay == A: delay(0.5)
                values[i], values[j] = values[j], values[i]
                print_list(i, j, values)
                delay(2)
            else:
                print_list(i, j, values)
                delay(2)
    return values


def final_print(l):
    clrscr()
    print("Sorted array : ",end=" ")
    for _ in l:
        print(colors.bg.light, colors.fg.red, _, end=" ")
    print(colors.bg.black, colors.fg.lightgrey)


if __name__ == '__main__':
    print("----------------------------------------------------")
    print("|            Bubble sort Visualization             |")
    print("----------------------------------------------------")
    print("   Enter Elements or Press Enter for random values  ")
    l = list(map(int, input(">> ").split()))
    if not l:
        l = [randint(-100, 100) for _ in range(0, int(input("Enter size : ")))]
    while True:
        delay = input("Automatic or Manual? (a/m) >>> ").upper()
        if delay in ['M', 'A']:
            delay = M if delay == "M" else A
            break

final_print(sort(l))

input()
