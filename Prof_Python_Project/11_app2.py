import tkinter as tk

def dispLabel():
    lbl.configure(text="안녕하세요")

root = tk.Tk()
root.geometry("300x200")

lbl = tk.Label(text="Label")
btn = tk.Button(text="push", command=dispLabel)

lbl.pack()
btn.pack()
tk.mainloop()