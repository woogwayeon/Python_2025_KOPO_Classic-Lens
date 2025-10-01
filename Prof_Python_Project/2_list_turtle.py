from turtle import *

shape("turtle")

col = ["orange", "limegreen", "yellow", "blue", "gold"]

for i in range(5):
    color(col[i])
    forward(200)
    left(144)
done()

# 만약 파일이 있다면 주소 넣고 꺼낼수도 있어요 그렇게 활용하세요