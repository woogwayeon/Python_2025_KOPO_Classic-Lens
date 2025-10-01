# pip install scikit-learn
import sklearn.datasets

digits = sklearn.datasets.load_digits()

print("데이터의 갯수=", len(digits.images))
print("이미지데이터=", digits.images[1700])
print("무슨숫자인가=", digits.target[1700])

# 0 > 0
# 1700 > 5가 나오네요