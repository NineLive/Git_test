"""
GUI based Calculator by Tkinter

Калькулятор с графикой на модуле Tkinter

Необходимо доделать:
- кнопку очистки
- обработка вещественных чисел (кнопко точки)
- при добавлении цифр к числу < 1 исчезает 0, из-за обработки стартового нуля (example: 0.53 => .5346)

"""

import tkinter as tk


def add_digit(digit):
    """
    Функция добавляющая цифру к текущему значению при вводе числа
    :param digit:
    :return:
    """
    value = label.cget('text')
    if value[0] == '0':
        value = value[1:]
    label['text'] = value + digit


def add_operation(operation):
    """
    Функция добавляющая операции над числами при вводе
    :param operation:
    :return:
    """
    value = label.cget('text')
    if value[-1] in '+-/*':
        value = value[:-1]
    label['text'] = value + operation


def calc():
    """
    Функция вычисляет результат выражения (функция кнопки =)
    :return:
    """
    value = str(eval(label.cget('text')))
    label['text'] = value


def make_negative():
    """
    Функция для получения отрицательных чисел (+/-)
    :return:
    """
    value = label.cget('text')
    if value[:1] == '-':
        label['text'] = value[1:]
    else:
        label['text'] = '-' + value


def make_digit_button(digit):
    """
    Функция создает кнопку с числом digit выполняющую add_digit()
    :param digit: число на кнопке
    :return: объект класса Button()
    """
    return tk.Button(root, text=digit, font='arial 14', command=lambda: add_digit(digit))


def make_operation_button(operation):
    """
    Функция создает кнопку с операцией operation и выполняющую add_operation()
    :param operation: операция на кнопке (+-*/)
    :return: объект класса Button()
    """
    return tk.Button(root, text=operation, font='arial 14', command=lambda: add_operation(operation))


def make_calc_button(operation):
    """
    Функция создает кнопку с операцией равно "operation" и выполняющую add_operation()
    :param operation: операция на кнопке (=)
    :return: объект класса Button()
    """
    return tk.Button(root, text=operation, font='arial 14', command=lambda: calc())


def make_negative_button(operation):
    """
    Функция создает кнопку для отрицательных чисел
    :param operation: ( +/- )
    :return: объект класса Button()
    """
    return tk.Button(root, text=operation, font='arial 14', command=lambda: make_negative())


root = tk.Tk()
label = tk.Label(root, font='arial 24')
label['text'] = '0'
label.grid(row=0, column=0, columnspan=4, sticky='nwes')

make_digit_button('1').grid(row=3, column=0, sticky='nwes')
make_digit_button('2').grid(row=3, column=1, sticky='nwes')
make_digit_button('3').grid(row=3, column=2, sticky='nwes')
make_digit_button('4').grid(row=2, column=0, sticky='nwes')
make_digit_button('5').grid(row=2, column=1, sticky='nwes')
make_digit_button('6').grid(row=2, column=2, sticky='nwes')
make_digit_button('7').grid(row=1, column=0, sticky='nwes')
make_digit_button('8').grid(row=1, column=1, sticky='nwes')
make_digit_button('9').grid(row=1, column=2, sticky='nwes')
make_digit_button('0').grid(row=4, column=1, sticky='nwes')
make_operation_button('+').grid(row=1, column=3, sticky='nwes')
make_operation_button('-').grid(row=2, column=3, sticky='nwes')
make_operation_button('*').grid(row=3, column=3, sticky='nwes')
make_operation_button('/').grid(row=4, column=3, sticky='nwes')
make_negative_button('+/-').grid(row=4, column=0, sticky='nwes')
make_calc_button('=').grid(row=4, column=2, sticky='nwes')


def main():
    """
    Главная функция содержит параметры окна, а также параметры оклонок и строк
    :return:
    """
    global root
    root.title('Calculator')
    root.resizable(False, False)
    root.grid_columnconfigure(0, minsize=100)
    root.grid_columnconfigure(1, minsize=100)
    root.grid_columnconfigure(2, minsize=100)
    root.grid_columnconfigure(3, minsize=100)
    root.grid_rowconfigure(1, minsize=50)
    root.grid_rowconfigure(2, minsize=50)
    root.grid_rowconfigure(3, minsize=50)
    root.grid_rowconfigure(4, minsize=50)
    root.mainloop()


main()

if __name__ == '__main__':
    main()
