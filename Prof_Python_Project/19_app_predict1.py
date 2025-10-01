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

    numImage = np.asarray(grayImage, dtype=float)
    numImage = np.floor(16 - 16 * (numImage / 256))
    numImage = numImage.flatten()

    return numImage


def predictDigits(data):
    # 16, 17, 18행이 모델링하는 과정
    digits = sklearn.datasets.load_digits()
    clf=sklearn.svm.SVC(gamma=0.001)
    clf.fit(digits.data, digits.target) # 피팅
    n = clf.predict([data])
    print("예측 = ", n)
    textLabel.configure(text="이 그림은"+str(n)+"입니다!")


def openFile():
    fpath = pd.askopenfilename()
    if fpath:
        data = dispPhoto(fpath)
        predictDigits(data)

root = tk.Tk()
root.geometry("400x400")

btn = tk.Button(text="파일열기", command=openFile)
imageLabel=tk.Label()

btn.pack()
imageLabel.pack()

textLabel = tk.Label(text = "손글씨 숫자를 인식합니다")
textLabel.pack()

tk.mainloop()