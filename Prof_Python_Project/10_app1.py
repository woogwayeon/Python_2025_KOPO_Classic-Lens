import tkinter as tk        # tkinter를 약칭으로

root = tk.Tk()
root.geometry("200x100")

lbl = tk.Label(text="서연선여넝")
btn = tk.Button(text="버튼")

lbl.pack()
btn.pack()
tk.mainloop()