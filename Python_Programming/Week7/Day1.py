## 디폴트 인수
print("---디폴트 인수 예제입니다.---")
def greet(name, msg="별일없죠?"):
    print("안녕", name + ' ' + msg)
greet("영희","좋은 아침!")
greet("영희")

## 위치인수와 키워드 인수
print("---위치인수와 키워드 인수 예제---")

def sub(x, y, z):
    print("x=", x, "y=", y, 'z=', z)
### 위치 인수, 순서 중요
sub(10, 20, 30)

### 키워드 인수, 순서 무관
sub(x=10, z=30, y=20)

### 혼합 사용, "위치인수" 뒤에 "키워드인수" 사용가능(vice-versa; 단, 무조건 위치인수가 먼저 와야함)
sub(10, y=20, z=30)
#sub(x=10, 20, 30)       ## SyntaxError: positional argument follows keyword argument

## 가변인수
print("---가변길이인수 예제---")
def varfunc(*args):
    print("인수의 타입은: ", type(args)) # args의 타입을 반환합니다. (튜플)
    print(args)
print("하나의 값으로 호출")
varfunc(10)
print("여러 개의 값으로 호출")
varfunc(10, 20, 30)
### 예제 - 전달하는 모든 값의 합을 계산
print("[Example] 전달하는 모든 값의 합을 계산하는 예제입니다.")
def add(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum
print(add(10, 20))
print(add(10,20,30))
print("---가변길이 키워드 인수 예제---")
def myfunc(**kwargs):
    result = ""
    print("인수의 타입은: ", type(kwargs)) # kwargs의 타입을 반환합니다.(딕셔너리)
    for arg in kwargs.values():
        result += arg
    return result

print(myfunc(a="Hi!", b="Mr.", c="Kim"))

# 언패킹
# print("---언패킹 예제입니다.---")
alist = [1, 2, 3]
print(*alist)   # 리스트가 아닌, 그 안의 객체들이 출력됩니다.
print(alist)

def sum(a, b, c):
    print(a+b+c)
alist = [1, 2, 3]
sum(*alist)
# sum(alist)      ## TypeError: sum() missing 2 required positional arguments: 'b' and 'c'

## Lab (p.221)
### "환영합니다" 문자열을 여러 번 출력하는 함수
print("[Example]'환영합니다' 문자열을 여러 번 출력하는 함수 예제입니다.")
def display(msg, count):
    for i in range(count):
        print(msg)
        i += 1;
    return msg

display("환영합니다.", 5)

## [직접 해보기] Lab (p.223)
### 현재 시급과 일한 시간 입력 받아 주급을 출력하는 함수입니다.
### weeklyPay(rate, hour)

# 5.6 결과 반환
## 결과 반환
def get_area1(radius):
    if radius > 0:
        return 3.14*radius**2
    else:
        return 0;
        exit(0)

st_area = get_area1(3)
print(st_area)

## Lab: 여러 개의 결과 값 반환 (p.227)
### 입력: 이름, 나이 => 동시 반환

def get_info():
    name = input("이름> ")
    age = int(input("나이> "))
    return name, age
st_name, st_age = get_info()
print("이름은 ", st_name, "이고 나이는 ", st_age, "살입니다.")

# 5.7 구조화
## Lab: 구조화 프로그래밍(p.232)
### 온도를 변환해주는 프로그램 작성

# 5.8 순환
## 예제 : 팩토리얼 계산 프로그램
def factorial(n):
    if n == 1:
        return(1)
    else:
        return n * factorial(n-1)
n = eval(input("정수를 입력하세요> "))      # eval() 정수변환; ans자열로 되어있는 코드나 수식등을 파이썬 코드처럼 실행할 때
print(n, "!= ", factorial(n))


## 실습
# def changeTemp():
#     if ()

def cToF(c):
    temp = c*9.0/5.0 + 32
    return temp

def fToC(f):
    temp = (f-32.0)*5.0/9.0
    return temp

def input_f():
    f = float(input("화씨 온도를 입력하시오> "))
    return f
def input_c():
    c = float(input("섭씨 온도를 입력하시오> "))
    return c

def main():
    while True:
        print(" 1. 섭씨온도 => 화씨온도 \n 2. 화씨 온도 => 섭씨온도 \n 3. 종료")
        choice = int(input("메뉴를 선택하세요> "))
        if choice == 1:
            t = input_c()
            t2 = cToF(t)
            print("화씨온도: ", t2)
        elif choice == 2:
            t = input_f()
            t2 = fToC(t)
            print("섭씨온도: ", t2)
        else:
            break

main()
