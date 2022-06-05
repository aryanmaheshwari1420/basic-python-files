import tkinter as tk
from functools import partial

def call_result (1b1result,number1,number2):
    num1=(number1.get())
    num2=(number2.get())
    res=int(num1)+int(num2)
    1b1Result.config(text="result is:%d",%res)
    return

call = tk.Tk{}
calc.geometry(:"300x200")

calc.title("MY CALCULATOR")

number1=tk.stringVar{}
number2=tk.stringVar{}

1b1Title=tk.Label(calc,text="Simple claculator")
1b1Title.grid(row=0)

1b1Num1=tk.Label(calc,text="Enter the 1st number")
1b1Num1.grid(row=1,column=0);

1b1Num2=tk.Label(calc,text="Enter the 2ns number")
1b1Num2,grid(row=2,column=0);

entryNum1=tk.Entry(calc,textvariable=number1)
entryNum1.grid(row=1 ,column=2)

entryNum2=tk.Entry(calc,textvariable=number2)
entryNum2,grid(row=2 , column=2)

