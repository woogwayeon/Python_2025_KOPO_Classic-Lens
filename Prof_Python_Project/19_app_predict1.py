import tkinter as tk
import tkinter.filedialog as pd
import PIL.Image
import PIL.ImageTk

import sklearn.datasets
import sklearn.svm
import numpy as np

def dispPhoto(path):
    # 이미지 읽어들인 뒤, 회색으로 변환함(이미지 변환 함수는 google에 무한히 많다)
    grayImage = PIL.Image.open(path).convert("L").resize((8, 8))

    dispImage=PIL.ImageTk.PhotoImage(grayImage.resize((300,300)))

    imageLabel.configure(image = dispImage)
    imageLabel.image = dispImage


def openFile():
    fpath = pd.askopenfilename()
    if fpath:
        data = dispPhoto(fpath)

root = tk.Tk()
root.geometry("400x400")

btn = tk.Button(text="파일열기", command=openFile)
imageLabel=tk.Label()

btn.pack()
imageLabel.pack()

tk.mainloop()