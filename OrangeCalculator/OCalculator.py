from tkinter import *

#Main window
root = Tk()
root.title("OrangeCalculator")
root.configure(bg="black")

#Entry bar
e = Entry(root, width=35, bd= 10, borderwidth=15, font=("Symbol", 14))
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#Image import
plus_img = PhotoImage(file=r"C:\Users\calle\Desktop\ITi\OrangeCalculator\img\plus.png")
minus_img = PhotoImage(file=r"C:\Users\calle\Desktop\ITi\OrangeCalculator\img\minus.png")
multi_img = PhotoImage(file=r"C:\Users\calle\Desktop\ITi\OrangeCalculator\img\multi.png")
div_img = PhotoImage(file=r"C:\Users\calle\Desktop\ITi\OrangeCalculator\img\div.png")
eq_img = PhotoImage(file=r"C:\Users\calle\Desktop\ITi\OrangeCalculator\img\equal.png")

#Actions
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "add"
    f_num = int(first_number)
    e.delete(0, END)

def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "sub"
    f_num = int(first_number)
    e.delete(0, END)

def button_multi():
    first_number = e.get()
    global f_num
    global math
    math = "multi"
    f_num = int(first_number)
    e.delete(0, END)

def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "div"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    secound_number = e.get()
    e.delete(0, END)
    if math == "add":
        e.insert(0, f_num + int(secound_number))

    if math == "sub":
        e.insert(0, f_num - int(secound_number))
    
    if math == "multi":
        e.insert(0, f_num * int(secound_number))
    
    if math == "div":
        e.insert(0, f_num / int(secound_number))

#Define buttons
button_1 = Button(root, text="1", padx=40, pady=20, bg="orange", command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, bg="orange", command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, bg="orange", command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, bg="orange", command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, bg="orange", command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, bg="orange", command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, bg="orange", command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, bg="orange", command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, bg="orange", command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, bg="orange", command=lambda: button_click(0))

button_add = Button(root, image=plus_img, padx=40, pady=20, bg="orange", command=button_add)
button_sub = Button(root, image=minus_img, padx=41, pady=20, bg="orange", command=button_sub)
button_multi = Button(root, image=multi_img, padx=41, pady=20, bg="orange", command=button_multi)
button_div = Button(root, image=div_img, padx=41, pady=20, bg="orange", command=button_div)
button_equal = Button(root, image=eq_img, padx=39, pady=20, bg="orange", command=button_equal)
button_clear = Button(root, text="C", padx=39, pady=20, bg="orange", command=button_clear)

#Put buttons on the screen
button_1.grid(row=3,column=0, pady=5)
button_2.grid(row=3,column=1, pady=5)
button_3.grid(row=3,column=2, pady=5)

button_4.grid(row=2,column=0, pady=5)
button_5.grid(row=2,column=1, pady=5)
button_6.grid(row=2,column=2, pady=5)

button_7.grid(row=1,column=0, pady=5)
button_8.grid(row=1,column=1, pady=5)
button_9.grid(row=1,column=2, pady=5)

button_0.grid(row=4,column=0, pady=5)

button_add.grid(row=1,column=3, pady=5)
button_sub.grid(row=2,column=3, pady=5)
button_multi.grid(row=3,column=3, pady=5)
button_div.grid(row=4,column=3, pady=5)
button_equal.grid(row=4,column=2, pady=5)
button_clear.grid(row=4,column=1, pady=5)

root.mainloop()