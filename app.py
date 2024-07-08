import ast
from tkinter import *

root = Tk()
root.geometry("600x400")
i = 0


def get_number(num):
    global i
    display.insert(i, num)
    i += 1


def get_operator(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length


def all_clear():
    display.delete(0, END)


def calculate():
    # entire_string = display.get()
    # node = ast.parse(entire_string, mode="eval")
    # result = eval(compile(node, '<string>', 'eval'))

    global i
    expression = display.get()
    try:
        result = eval(expression)
        display.delete(0, END)
        display.insert(0, result)
        i = len(str(result))
    except Exception as e:
        display.delete(0, END)
        display.insert(0, "Error")
        i = 0


def delete_last():
    global  i
    current_text= display.get()
    if current_text:
        new_text = current_text[:-1]
        display.delete(0, END)
        display.insert(0, new_text)
        i -= 1


display = Entry(root)
display.grid(row=1, columnspan=6)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0
for x in range(3):
    for y in range(3):
        button_text = numbers[counter]
        button = Button(root, text=button_text, width=4, height=2, command=lambda text=button_text: get_number(text))
        button.grid(row=x + 2, column=y)
        counter += 1
button = Button(root, text="0", width=4, height=2, command=lambda: get_number(0))
button.grid(row=5, column=1)
count = 0
operations = ['+', '-', '*', '/', '%', '*3.14', '**', '**2', '(', ')', ]
for x in range(4):
    for y in range(3):
        if count < len(operations):
            button = Button(root, text=operations[count], width=4, height=2,
                            command=lambda text=operations[count]: get_operator(text))
            count += 1
            button.grid(row=x + 2, column=y + 3)

Button(root, text="AC", width=4, height=2, command=all_clear).grid(row=5, column=0)
Button(root, text="=", width=4, height=2, command=calculate).grid(row=5, column=2)
Button(root, text="⌫", width=4, height=2, command=delete_last).grid(row=5, column=4)
root.mainloop()
