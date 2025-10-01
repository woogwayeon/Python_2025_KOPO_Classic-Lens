import sklearn.datasets
import sklearn.svm
import PIL.Image
import numpy as np # 넘파이는 매트릭스 / 판다스는 데이터프레임

def imageToData(fileName):
    grayImage = PIL.Image.open(fileName).convert("L").resize((8,8))

    numImage = np.asarray(grayImage, dtype=float)
    numImage=np.floor(16-16*(numImage/256))
    numImage=numImage.flatten()
    
    return numImage


def predictDigits(data):
    # 16, 17, 18행이 모델링하는 과정
    digits = sklearn.datasets.load_digits()
    clf=sklearn.svm.SVC(gamma=0.001)
    clf.fit(digits.data, digits.target) # 피팅

    n = clf.predict([data])
    print("예측 = ", n)

# 데이터를 가져와서 벡터 데이터로 만든것
data = imageToData("D:/2025_KoSeoyeon/2 _Semester/sampledata/숫자 (1).png")
predictDigits((data))