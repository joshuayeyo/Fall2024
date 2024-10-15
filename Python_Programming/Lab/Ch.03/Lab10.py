# page 145
## 올바른 삼각형 구별하기

a = int(input("삼각형의 한 변을 입력하세요> "))
b = int(input("삼각형의 한 변을 입력하세요> "))
c = int(input("삼각형의 한 변을 입력하세요> "))

if (a+b>c and a+c>b and b+c>a):
    print("올바른 삼각형입니다.")
else: 
    print("잘못된 삼각형입니다.")