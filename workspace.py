import tkinter as tk
from warnings import catch_warnings

#text field
field_txt=""
def add_text(sth):
    global field_txt
    field_txt=field_txt+str(sth)
    field.delete(1.0, "end")
    field.insert(1.0, field_txt)
def calculate():
    global field_txt
    try:
        result=eval(field_txt)
        field.delete(1.0,"end")
        field.insert(1.0,result)
    except:
        field.delete(1.0,"end")
        field.insert(1.0,"Error")
def clear():
    global field_txt
    field_txt=""
    field.delete(1.0,"end")


#window
window=tk.Tk()
window.geometry("300x300")
field=tk.Text(window,height=2,width=21, font=("Arial", 15), bg="black", fg="white")
field.grid(row=1, column=1, columnspan=5)
window.title("Calculator")
window.configure(bg="light grey")
#buttons
btn_0=tk.Button(window,text="0", command=lambda: add_text(0), height=1, width=6, font=("Arial", 15), bg="black", fg="white")
btn_0.grid(row=6,column=1, columnspan=2)
btn_1=tk.Button(window,text="1", command=lambda: add_text(1), height=1, width=3, font=("Arial", 15), bg="black", fg="white")
btn_1.grid(row=5,column=1)
btn_2=tk.Button(window,text="2", command=lambda: add_text(2), height=1, width=3, font=("Arial", 15), bg="black", fg="white")
btn_2.grid(row=5,column=2)
btn_3=tk.Button(window,text="3", command=lambda: add_text(3), height=1, width=3, font=("Arial", 15), bg="black", fg="white")
btn_3.grid(row=5,column=3)
btn_4=tk.Button(window,text="4", command=lambda: add_text(4), height=1, width=3, font=("Arial", 15), bg="black", fg="white")
btn_4.grid(row=4,column=1)
btn_5=tk.Button(window,text="5", command=lambda: add_text(5), height=1, width=3, font=("Arial", 15), bg="black", fg="white")
btn_5.grid(row=4,column=2)
btn_6=tk.Button(window,text="6", command=lambda: add_text(6), height=1, width=3, font=("Arial", 15), bg="black", fg="white")
btn_6.grid(row=4,column=3)
btn_7=tk.Button(window,text="7", command=lambda: add_text(7), height=1, width=3, font=("Arial", 15), bg="black", fg="white")
btn_7.grid(row=3,column=1)
btn_8=tk.Button(window,text="8", command=lambda: add_text(8), height=1, width=3, font=("Arial", 15), bg="black", fg="white")
btn_8.grid(row=3,column=2)
btn_9=tk.Button(window,text="9", command=lambda: add_text(9), height=1, width=3, font=("Arial", 15), bg="black", fg="white")
btn_9.grid(row=3,column=3)
#operators
btn_plus=tk.Button(window,text="+", command=lambda: add_text("+"), height=1, width=3, font=("Arial", 15), bg="grey", fg="black")
btn_plus.grid(row=4,column=4)
btn_minus=tk.Button(window,text="-", command=lambda: add_text("-"), height=1, width=3, font=("Arial", 15), bg="grey", fg="black")
btn_minus.grid(row=5,column=4)
btn_multiply=tk.Button(window,text="*", command=lambda: add_text("*"), height=1, width=3, font=("Arial", 15), bg="grey", fg="black")
btn_multiply.grid(row=3,column=4)
btn_divide=tk.Button(window,text="/", command=lambda: add_text("/"), height=1, width=3, font=("Arial", 15), bg="grey", fg="black")
btn_divide.grid(row=2,column=4)
btn_percent=tk.Button(window,text="%", command=lambda: add_text("%"), height=1, width=3, font=("Arial", 15), bg="grey", fg="black")
btn_percent.grid(row=2,column=3)
btn_decimal=tk.Button(window,text=".", command=lambda: add_text("."), height=1, width=3, font=("Arial", 15), bg="grey", fg="black")
btn_decimal.grid(row=6,column=3)
btn_clear=tk.Button(window,text="C", command=clear, height=1, width=6, font=("Arial", 15), bg="grey", fg="black")
btn_clear.grid(row=2,column=1, columnspan=2)
btn_equal=tk.Button(window,text="=", command=calculate, height=1, width=3, font=("Arial", 15), bg="grey", fg="black")
btn_equal.grid(row=6,column=4)
btn_bracket1=tk.Button(window,text="(", command=lambda: add_text("("), height=1, width=3, font=("Arial", 15), bg="grey", fg="black")
btn_bracket1.grid(row=2,column=5)
btn_bracket2=tk.Button(window,text=")", command=lambda: add_text(")"), height=1, width=3, font=("Arial", 15), bg="grey", fg="black")
btn_bracket2.grid(row=3,column=5)
window.mainloop()