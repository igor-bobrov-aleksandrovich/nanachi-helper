from tkinter import *
from tkinter import ttk

def finish():
    root.destroy()  # ручное закрытие окна и всего приложения
    print("Закрытие приложения")

def hide():
    pass
def __init_view__():
    root = Tk()
    root.title("Nanachi")
    root.geometry("400x600+0+250")
    root.protocol("WM_DELETE_WINDOW", finish)
    root.attributes("-toolwindow", True)
    root.attributes("-alpha", 0.9)
    root.resizable(False, False)

    root.overrideredirect(1)

    btn = ttk.Button(text="X", command=finish)
    #btn.pack(anchor=W, ipadx=0, ipady=30, padx=[0, 0])
    btn.grid(row=0, column=0, ipadx=0, ipady=30)
    btn = ttk.Button(text="<<", command=hide)
    #btn.pack(anchor=W, ipadx=0, ipady=170, padx=[0, 0])
    btn.grid(row=1, column=0, ipadx=0, ipady=245)

    btn = ttk.Button(text="Задать запрос", command=hide)
    #btn.pack(anchor=S, ipadx=200)
    btn.grid(row=0, column=1, rowspan=2, ipadx=120, sticky=S)

    root.configure(bg='black')
    root.mainloop()

