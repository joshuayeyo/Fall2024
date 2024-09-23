# 4
radius = float(input("원의 반지름을 입력하세요> "))
if (radius < 0 ) :
    print("양수를 입력하세요.")
    print("프로그램을 재시작하세요.")
else :
    print("원의 면적: ", round(radius**2*3.14, 2))
# 6
import random  # 랜덤 모듈을 임포트합니다. 랜덤 모듈은, 이름 그대로 난수를 다룰 수 있는 모듈입니다.

computer = random.randint(1, 3)  # 1부터 3까지의 정수 중 하나를 computer 변수에 할당합니다.

user_input = int(input("다음 중 하나의 값을 선택하세요.(1: 가위, 2:바위, 3:보) > "))
if (user_input < 1 or user_input > 3) :
    print("올바른 값을 입력하세요.")
    print("프로그램을 다시 시작하세요.")
    exit(1)  # 프로그램이 에러가 발생하는 등 비정상적으로 종료되는 경우입니다. exit 함수를 통해 프로그램을 종료할 수 있습니다.
if (computer == 1) :
    print("컴퓨터는 가위를 냈습니다.")
    if (user_input == 1) :
        print("유저는 컴퓨터와 비겼습니다.")
    elif (user_input == 2) :
        print("유저는 컴퓨터에게 이겼습니다.")
    elif (user_input == 3) :
        print("유저는 컴퓨터에게 졌습니다.")
elif (computer == 2) :
    print("컴퓨터는 바위를 냈습니다.")
    if (user_input == 1) :
        print("유저는 컴퓨터에게 졌습니다.")
    elif (user_input == 2) :
        print("유저는 컴퓨터와 비겼습니다.")
    elif (user_input == 3) :
        print("유저는 컴퓨터에게 이겼습니다.")
elif (computer == 3) :
    print("컴퓨터는 보를 냈습니다.")
    if (user_input == 1) :
        print("유저는 컴퓨터에게 이겼습니다..")
    elif (user_input == 2) :
        print("유저는 컴퓨터에게 졌습니다.")
    elif (user_input == 3) :
        print("유저는 컴퓨터와 비겼습니다.")
print("프로그램을 종료합니다.")

# 8

weight, height = eval(input("체중과 키를 입력하세요(체중, 키)> "))

standard_weight = (height-100)*0.9

if standard_weight < weight :
    print("과체중입니다.")
elif standard_weight == weight :
    print("표준입니다.")
elif standard_weight > weight :
    print("저체중입니다.")
else :
    print("값을 잘못 입력했습니다. 체중과 키를 입력하세요.")
    print("프로그램을 종료합니다.")
    exit(0)

# 14

a = float(input("a를 입력하세요.>"))
b = float(input("b를 입력하세요.>"))
c = float(input("c를 입력하세요.>"))

discriminant = b**2-4*a*c #이차방정식 판별식

if discriminant > 0:
    var1 = ((-b)+((b**2-4*a*c)**0.5))/(2*a)  # 근의 공식, 소수점 2자리에서 반올림
    var2 = ((-b)-((b**2-4*a*c)**0.5))/(2*a)
    print("실근은 %lf와 %lf입니다." %(var1, var2))
elif discriminant == 0:
    var3 = 2*a/-b
    print("실근은 %lf입니다." %var3)
else:
    print("실근은 존재하지 않습니다.")

# 16

pH = float(input("pH를 입력하세요> ")) # float값을 입력받는다.

if (pH < 7 and pH >= 0):  # 에디터 테마 문제로 인해, 크거나 같다라는 표시가 >=로 인식되는 오류가 있습니다.
    print("산입니다.")
elif (pH >= 8 and pH <= 14):
    print("알칼리입니다.")
elif (7 <= pH < 8):  # 값이 소수점인 경우를 위해 7과 8 사이로 받는다.
    print("중성입니다.")
else:
    print("프로그램을 종료합니다. 다시 시작하세요.")
    exit(1)
