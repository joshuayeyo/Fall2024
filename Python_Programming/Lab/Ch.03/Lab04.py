# page 132
## 물의 상태 출력하기

userInput = int(input("물의 온도를 입력하시오> "))

if (userInput <= 0):
    print("얼음입니다.")
elif (0 < userInput and userInput < 100):
    print("액체입니다.")
else:
    print("기체입니다.")