import os
import numpy as np
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
import joblib

# ===== 경로 설정 =====
DATASET_DIR = "./data-img"
MODEL_DIR = "./models"
MODEL_PATH = os.path.join(MODEL_DIR, "svm_image_era.pkl")

# ===== 이미지 불러오기 =====
def load_images():
    data = []
    labels = []
    for era in os.listdir(DATASET_DIR):
        era_path = os.path.join(DATASET_DIR, era)
        if not os.path.isdir(era_path):
            continue

        for file in os.listdir(era_path):
            if not (file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg")):
                continue
            fpath = os.path.join(era_path, file)
            img = Image.open(fpath).convert("L").resize((640, 640))
            arr = np.array(img).flatten() / 255.0
            data.append(arr)
            labels.append(era)
    return np.array(data), np.array(labels)

# ===== 한글 classification_report 출력 함수 추가됨 =====
def print_korean_report(y_true, y_pred):  # 추가됨
    report = classification_report(y_true, y_pred)
    report = report.replace("precision", "정밀도")
    report = report.replace("recall", "재현율")
    report = report.replace("f1-score", "F1 점수")
    report = report.replace("support", "지원 수")
    print("\n분류 리포트")
    print(report)
# ==================================================

# ===== 학습 =====
def train_model():
    print("Loading score images...")
    X, y = load_images()
    print(f"Total {len(X)} images loaded")

    # stratify=y 추가로 클래스 비율 유지 (변경됨)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
    # ==================================================

    print("Training SVM model...")
    clf = SVC(kernel="rbf", gamma=0.001, probability=True)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {acc:.2f}")

    # 한글 리포트 출력 (추가한 함수 사용)
    print_korean_report(y_test, y_pred)  # 추가됨

    os.makedirs(MODEL_DIR, exist_ok=True)
    joblib.dump(clf, MODEL_PATH)
    print(f"Model saved to: {MODEL_PATH}")

if __name__ == "__main__":
    train_model()
