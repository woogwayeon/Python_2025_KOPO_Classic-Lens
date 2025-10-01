import tkinter as tk
import random

def dispLabel():
    list_unse = ["완전대길", "대길", "소길", "잘될것임"]
    lbl.configure(text=random.choice(list_unse))
    
root=tk.Tk()
root.geometry("600x400")

lbl = tk.Label(text="라벨")
btn = tk.Button(text="운세확인하기", command=dispLabel)

lbl.pack()
btn.pack()
tk.mainloop()
