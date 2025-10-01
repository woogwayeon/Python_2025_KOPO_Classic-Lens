import tkinter as tk
import tkinter.filedialog as pd

# PIL : pip install pillow
import PIL.Image
import PIL.ImageTk

def dispPhoto(path):
    newImg = PIL.Image.open(path).resize((300, 300))
    imgData = PIL.ImageTk.PhotoImage(newImg)
    imageLabel.configure(image = imgData)
    imageLabel.image = imgData

def openFile():
    fpath = pd.askopenfilename()
    if fpath:
        dispPhoto(fpath)

root = tk.Tk()
root.geometry("400x350")

btn = tk.Button(text="파일열기", command=openFile)
imageLabel=tk.Label()

btn.pack()
imageLabel.pack()
tk.mainloop()