import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import joblib

# 경로 설정
MODEL_PATH = "./models/svm_image_era.pkl"

# 모델 로드
model = joblib.load(MODEL_PATH)
eras = ["renaissance", "baroque", "classical", "romantic", "modern"]

# 예측 함수
def predict_image(path):
    img = Image.open(path).convert("L").resize((64, 64))
    arr = np.array(img).flatten() / 255.0
    pred = model.predict([arr])[0]
    prob = model.predict_proba([arr])[0]
    confidence = np.max(prob) * 100
    return pred, confidence

# 이미지 선택
def open_image():
    file_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=(("Image Files", "*.png;*.jpg;*.jpeg"),)
    )
    if not file_path:
        return

    # 이미지 표시
    img = Image.open(file_path)
    img_resized = img.resize((256, 256))
    img_tk = ImageTk.PhotoImage(img_resized)
    image_label.configure(image=img_tk)
    image_label.image = img_tk

    # 예측 수행
    pred, conf = predict_image(file_path)
    result_label.config(text=f"{pred} 시대의 곡으로 ({conf:.1f}% 예측되었습니다)")


# GUI
root = tk.Tk()
root.title("ClassicLens")
root.geometry("500x500")

title_label = tk.Label(root, text="🎼 ClassicLens", font=("Noto Sans KR", 18, "bold"))
title_label.pack(pady=10)

btn = tk.Button(root, text="악보 가져오기", command=open_image, width=25, height=2)
btn.pack(pady=10)

image_label = tk.Label(root)
image_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Noto Sans KR", 14))
result_label.pack(pady=10)

root.mainloop()