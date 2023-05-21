from tkinter import *

root = Tk()
root.title('Calculator')
root.geometry('330x370')
root.resizable(0,0)

root.configure(background='#F0F0F0')

# Create Entry widget for displaying the result
result_label = Entry(root, width=20, font=('Arial', 20), bd=5, justify=RIGHT)
result_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Initialize the global variables
first_number = ""
operator = ""

# Function to handle button clicks
def button_click(number):
    current = result_label.get()
    result_label.delete(0, END)
    result_label.insert(0, current + str(number))

def button_clear():
    result_label.delete(0, END)
    global first_number, operator
    first_number = ""
    operator = ""

def button_operator(op):
    global first_number, operator
    first_number = result_label.get()
    operator = op
    result_label.delete(0, END)

def button_equal():
    second_number = result_label.get()
    result_label.delete(0, END)

    if operator == "+":
        result = float(first_number) + float(second_number)
    elif operator == "-":
        result = float(first_number) - float(second_number)
    elif operator == "*":
        result = float(first_number) * float(second_number)
    elif operator == "/":
        result = float(first_number) / float(second_number)

    result_label.insert(0, str(result))

# Create number buttons
for i in range(9):
    row = i // 3 + 1
    col = i % 3
    btn = Button(root, text=str(i + 1), padx=20, pady=10, font=('Arial', 14),
                 command=lambda num=i+1: button_click(num))
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.configure(background='#D3D3D3', fg='black')

# Create operator buttons
operators = ['+', '-', '*', '/']
for i, op in enumerate(operators):
    btn = Button(root, text=op, padx=20, pady=10, font=('Arial', 14),
                 command=lambda opr=op: button_operator(opr))
    btn.grid(row=i + 1, column=3, padx=5, pady=5)
    btn.configure(background='#FFA500', fg='white')

# Create other buttons
btn_0 = Button(root, text='0', padx=20, pady=10, font=('Arial', 14),
               command=lambda: button_click(0))
btn_0.grid(row=4, column=0, padx=5, pady=5)
btn_0.configure(background='#D3D3D3', fg='black')

btn_decimal = Button(root, text='.', padx=20, pady=10, font=('Arial', 14),
                     command=lambda: button_click('.'))
btn_decimal.grid(row=4, column=1, padx=5, pady=5)
btn_decimal.configure(background='#D3D3D3', fg='black')

btn_clear = Button(root, text='C', padx=20, pady=10, font=('Arial', 14),
                   command=button_clear)
btn_clear.grid(row=4, column=2, padx=5, pady=5)
btn_clear.configure(background='#FFA500', fg='white')

btn_equal = Button(root, text='=', padx=20, pady=10, font=('Arial', 14),
                   command=button_equal)
btn_equal.grid(row=4, column=3, padx=5, pady=5)
btn_equal.configure(background='#FFA500', fg='white')

root.mainloop()

