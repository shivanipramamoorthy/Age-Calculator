import tkinter as tk
from datetime import datetime
def calculate_age():
    birth_year=input1.get()
    try:
        birth_year=int(birth_year)
        current_year=datetime.now().year
        age1=current_year-birth_year
        age.config(text=f"your age is:{age1} years")
    except ValueError:
        age.config("please enter a valid year")
calculator=tk.Tk()
calculator.geometry("10000x10000")
calculator.config(bg="white")
label1=tk.Label(calculator,text="enter your birthyear below!!!",fg="black",bg="white")
label1.pack(pady=70)
input1=tk.Entry(calculator,fg="black",bg="white")
input1.pack(pady=90)
button1=tk.Button(calculator,text="enter",fg="black",bg="white",command=calculate_age)
button1.pack(pady=110)
age=tk.Label(calculator,text="",fg="black",bg="white")
age.pack(pady=120)
calculator.mainloop()
