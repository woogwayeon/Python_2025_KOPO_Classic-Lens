# 노트북 글자 깨짐 때문에 추가
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(2)

# 기본 import
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import joblib
import webbrowser

# 경로 설정
MODEL_PATH = "./models/svm_image_era.pkl"

# 모델 가져오기
model = joblib.load(MODEL_PATH)
periods = ["renaissance", "baroque", "classical", "romantic", "modern"]

# 시대별 설명 및 대표 작곡가
period_info = {
    "renaissance": {
        "kor": "르네상스 시대",
        "desc": "복잡한 폴리포니(다성음악)가 발전한 시기입니다. 종교음악이 중심이었으며,"
                "인간의 감정보다는 조화로운 구조가 강조되었습니다.",
        "composer": "팔레스트리나, 조스캥 데 프레, 토마스 탤리스"
    },

    "baroque": {
        "kor": "바로크 시대",
        "desc": "화려하고 장식적인 음악 양식이 등장했습니다. 대위법과 통주저음이 발전하며,"
                "오페라와 협주곡이 본격적으로 등장했습니다.",
        "composer": "바흐, 헨델, 비발디"
    },

    "classical": {
        "kor": "고전주의 시대",
        "desc": "형식미와 균형이 중요하게 여겨졌습니다. 교향곡, 소나타 등의 장르가 확립되었으며,"
                "명료한 선율과 구조가 특징입니다.",
        "composer": "하이든, 모차르트, 베토벤"
    },

    "romantic": {
        "kor": "낭만주의 시대",
        "desc": "개인 감정과 표현이 중심이 된 시대입니다."
                "자유로운 형식과 감성적 멜로디가 특징이며,"
                "음악이 문학, 회화 등과도 긴밀히 연결되었습니다.",
        "composer": "쇼팽, 리스트, 슈만, 브람스, 차이콥스키"
    },

    "modern": {
        "kor": "근현대 시대",
        "desc": "전통적 조성을 벗어나 다양한 음악 실험이 이루어졌습니다."
                "인상주의, 표현주의, 전자음악 등 새로운 장르가 등장했습니다.",
        "composer": "드뷔시, 스트라빈스키, 쇤베르크"
    }
}


# 예측 함수
def predict_image(path):
    img = Image.open(path).convert("L").resize((320, 320))
    arr = np.array(img).flatten() / 255.0
    pred = model.predict([arr])[0]
    return pred, None

# 구글 검색
def open_google_search(keyword):
    webbrowser.open(f"https://www.google.com/search?q={keyword}+음악")

def create_round_shadow_button(text, command):
    frame = tk.Frame(root, bg="#f8f9fa")

    btn = tk.Button(frame, text=text, command=command,
                    width=24, height=2,
                    bg="#ffffff", fg="#212529",
                    font=("Pretendard", 13, "bold"),
                    relief="flat", bd=1,
                    highlightbackground="#d0d4d9",
                    activebackground="#eeeeee")
    btn.pack()

    # Hover
    btn.bind("<Enter>", lambda e: btn.config(bg="#444444", fg="#ffffff"))
    btn.bind("<Leave>", lambda e: btn.config(bg="#ffffff", fg="#212529"))

    frame.inner_btn = btn
    return frame

# 이미지 선택
def open_image():
    file_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=(("Image Files", "*.png;*.jpg;*.jpeg"),)
    )
    if not file_path:
        return

    img = Image.open(file_path).resize((256, 256))
    img_tk = ImageTk.PhotoImage(img)
    image_label.configure(image=img_tk)
    image_label.image = img_tk

    pred, _ = predict_image(file_path)
    info = period_info.get(pred)

    result_label.config(text=f"{info['kor']}의 악보로 판정됩니다!")
    desc_label.config(text=f"{info['kor']}에는 {info['desc']}")
    composer_label.config(text=f"대표 작곡가: {info['composer']}")

    search_btn.inner_btn.config(command=lambda: open_google_search(info["kor"]))
    search_btn.pack(pady=10)

# GUI 설정
root = tk.Tk()
root.title("ClassicLens")
root.configure(bg="#f8f9fa")
root.geometry("520x800")

title_label = tk.Label(
    root,
    text="🎼 ClassicLens",
    font=("Pretendard", 18, "bold"),
    bg="#f8f9fa",
    fg="#212529"
)
title_label.pack(pady=25)

btn = create_round_shadow_button("악보 가져오기", open_image)
btn.pack(pady=10)

image_label = tk.Label(root, bg="#f8f9fa")
image_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Pretendard", 14), bg="#f8f9fa", fg="#343a40")
result_label.pack(pady=10)

desc_label = tk.Label(root, text="", wraplength=480, font=("Pretendard", 11),
                      justify="center", bg="#f8f9fa")
desc_label.pack(pady=10)

composer_label = tk.Label(root, text="", font=("Pretendard", 11), bg="#f8f9fa")
composer_label.pack(pady=10)

search_btn = create_round_shadow_button("🔎 구글에서 더 알아보기", lambda: None)
search_btn.pack_forget()

root.mainloop()
