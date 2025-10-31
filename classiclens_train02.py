import os
import numpy as np
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
import joblib

# 경로 설정
DATASET_DIR = "./data-img"
MODEL_DIR = "./models"
MODEL_PATH = os.path.join(MODEL_DIR, "svm_image_era.pkl")

# 이미지(학습데이터)
def load_images():
    data = []
    labels = []
      for era in os.listdir(DATASET_DIR):
        
        era_path = os.path.join(DATASET_DIR, era)
        
        if not os.path.isdir(era_path):
            continue

        for file in os.listdir(era_path):
            
            # 대소문자 구분없이 확장자 체크 (251021-수정됨)
            if not (file.lower().endswith(".png") or 
                file.lower().endswith(".jpg") or 
                file.lower().endswith(".jpeg")):
                
                continue

            fpath = os.path.join(era_path, file)
            img = Image.open(fpath).convert("L").resize((320, 320))
            arr = np.array(img).flatten() / 255.0
            data.append(arr)
            labels.append(era)

    return np.array(data), np.array(labels)

# 한글로 좀 나오게 해주세요
def print_korean_report(y_true, y_pred):
    report = classification_report(y_true, y_pred)
    report = report.replace("precision", "정밀도")
    report = report.replace("recall", "재현율")
    report = report.replace("f1-score", "F1 점수")
    report = report.replace("support", "지원 수")
    print("\n분류 리포트")
    print(report)


# 학습시작!
def train_model():
    print("loading images")
    X, y = load_images()
    print(f"total {len(X)} image")

    # stratify=y (데이터 학습시 원래 분포 그대로 유지)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

    print("SVM모델 학습")
    clf = SVC(kernel="rbf", gamma=0.001, probability=True, class_weight='balanced')
    
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {acc:.2f}")

    print_kor(y_test, y_pred)

    os.makedirs(MODEL_DIR, exist_ok=True)   # 모델을 저장할 폴더가 없으면 자동으로 만들기
    joblib.dump(clf, MODEL_PATH)            # 학습된 모델 객체(clf)를 위치에 파일로 저장
    print(f"Model saved to: {MODEL_PATH}")  # 모델 저장경로 확인


if __name__ == "__main__":
    train_model()
