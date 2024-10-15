# page 75
## 원기둥의 부피 계산하기
### 원지름의 부피 V=3.14*h*r^2
radius = int(input("반지름을 입력하세요> "))
height = int(input("높이를 입력하ㅔ요> "))
PI = 3.14

volume = radius**2*height*PI

print(f'원기둥의 부피는> {volume}')
