# creating an interactive counter that will increase and decrease respectively of their buttons

# Author: Marlon Chhour
# Date Completed: 9/02/21

import tkinter as tk

window = tk.Tk()
window.title("tkinter counter")
window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

# on click of + button; counter label will increase by 1
def increase():
    value = int(count["text"])
    count["text"] = f"{value + 1}"

# on click of - button; counter label will decrease by 1
def decrease():
    value = int(count["text"])
    count["text"] = f"{value - 1}"

buttonDecrease = tk.Button(master=window, text="-", command=decrease)
buttonDecrease.grid(row=0, column=0, sticky='nsew')

count = tk.Label(master=window, text="0")
count.grid(row=0, column=1)

buttonIncrease = tk.Button(master=window, text='+', command=increase)
buttonIncrease.grid(row=0, column=2, sticky='nsew')

window.mainloop()