from tkinter import Tk, Button, Entry, Label
from math_core import sqrt_number
from errors import safe_calculate
from app_language import load, current

load("ru")

# окно
window = Tk()
window.geometry("400x300")

#элементы окна
entry = Entry(window)
entry.pack(pady=10)

result_label = Label(window, text="")
result_label.pack(pady=10)

#вычисление
def calculate():
    def work():
        x = float(entry.get())
        return sqrt_number(x)

    result = safe_calculate(work)
    result_label.config(text=str(result))

button_calc = Button(window, command=calculate)
button_calc.pack(pady=10)

#обновление языка
def update_language():
    window.title(current["title"])
    button_calc.config(text=current["button"])
    result_label.config(text=current["result"])

#кноки языка
def switch_to_ru():
    load("ru")
    update_language()

def switch_to_en():
    load("en")
    update_language()

lang_ru = Button(window, text="RU", command=switch_to_ru)
lang_en = Button(window, text="EN", command=switch_to_en)

lang_ru.pack(side="left", padx=20, pady=20)
lang_en.pack(side="right", padx=20, pady=20)

#апдейт
update_language()

window.mainloop()