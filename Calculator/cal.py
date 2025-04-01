from tkinter import *

class Calculator:
    def __init__(self, master):
        master.title("CALCULATOR")
        master.geometry("390x440+0+0")
        master.config(bg="black")
        master.resizable(False, False)
        self.equation = StringVar()
        self.entry_value = ""
        Entry(width=17,  bg='#fff', font=('arial bold', 28), textvariable=self.equation).place(x=13, y=10)
        Button(width=11, height=4, text="%", relief="raised",font=("bold",15), bg="black",fg="white", command=lambda: self.show('%')).place(x=180, y=50)
        Button(width=11, height=4, text="1", relief="raised",font=("bold",15), bg="black",fg="white", command=lambda: self.show(1)).place(x=0, y=125)
        Button(width=11, height=4, text="2", relief="raised",font=("bold",15), bg="black",fg="white", command=lambda: self.show(2)).place(x=90, y=125)
        Button(width=11, height=4, text="3", relief="raised",font=("bold",15), bg="black",fg="white", command=lambda: self.show(3)).place(x=180, y=125)
        Button(width=11, height=4, text="4", relief="raised",font=("bold",15), bg="black",fg="white", command=lambda: self.show(4)).place(x=0, y=200)
        Button(width=11, height=4, text="5", relief="raised",font=("bold",15), bg="black",fg="white", command=lambda: self.show(5)).place(x=90, y=200)
        Button(width=11, height=4, text="6", relief="raised",font=("bold",15), bg="black",fg="white", command=lambda: self.show(6)).place(x=180, y=200)
        Button(width=11, height=4, text="7", relief="raised",font=("bold",15), bg="black",fg="white", command=lambda: self.show(7)).place(x=0, y=275)
        Button(width=11, height=4, text="8", relief="raised",font=("bold",15), bg="black",fg="white", command=lambda: self.show(8)).place(x=90, y=275)
        Button(width=11, height=4, text="9", relief="raised",font=("bold",15), bg="black",fg="white", command=lambda: self.show(9)).place(x=180, y=275)
        Button(width=11, height=4, text="0", relief="raised",font=("bold",15), bg="black",fg="white", command=lambda: self.show(0)).place(x=0, y=350)
        Button(width=11, height=4, text=".", relief="raised",font=("bold",15), bg="black",fg="white", command=lambda: self.show('.')).place(x=90, y=350)
        Button(width=11, height=4, text="+", relief="raised",font=("bold"), bg="black",fg="white", command=lambda: self.show('+')).place(x=270, y=275)
        Button(width=11, height=4, text="-", relief="raised",font=("bold"), bg="black",fg="white", command=lambda: self.show('-')).place(x=270, y=200,height=75)
        Button(width=11, height=4, text="/", relief="raised",font=("bold",15), bg="black",fg="white", command=lambda: self.show('/')).place(x=270, y=50)
        Button(width=11, height=4, text="x", relief="raised",font=("bold"), bg="black",fg="white", command=lambda: self.show('*')).place(x=270, y=125,height=75)
        Button(width=11, height=4, text="=", relief="raised",font=("bold",15), bg="white",fg="black", command=self.solve).place(x=180, y=350,width=220)
        Button(width=11, height=4, text="C", relief="raised",font=("bold"), bg="yellow",fg="black", command=self.clear).place(x=0, y=50,width=180,height=75)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ""
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
        except Exception as e:
            self.equation.set("Error")

root = Tk()
calculator = Calculator(root)
root.mainloop()