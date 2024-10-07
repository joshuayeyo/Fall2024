# 문자열 내장함수
print(chr(97))
print(ord("a"))

# 문자열 인덱싱
s = "Monthy Python"
s[0]
print(s[0])

# 문자열 슬라이싱
s[6:10]
print(s[6:10])
print(s[:2])
print(s[4:])
print(s[:2]+s[2:])
print(s[:])

reg = "100724"
month = reg[:2]
print("Month>", month)
day = reg[2:4]
print("Day", day)
year = reg[4:6]
print("Year=", year)

# 문자열은 불변객체이다.
word = "abcdef"
# word[0] = "A"
word = "A" + word[1:]
print(word)

# 문자열 비교
a = input("문자열을 입력하시오> ")
b = input("문자열을 입력하시오> ")

if (a < b):
    print(a, "가 앞에 있다.")
else:
    print(b, "가 앞에 있다.")

# 문자열 출력
## f-문자열
x = 25
y = 98
prod = x * y
print(f"{x}와 {y}의 곱은 {prod}")

# 대소문자 변환
s = "i am a student"
s_upper = s.capitalize()
print(s, s_upper)

s_lower = s_upper.lower()
print(s_upper, s_lower)

# 찾기 / 바꾸기
s = input("파이썬 소스파일 이름을 입력하시오> ")
if s.endswith(".py"):
    print("올바른 파일 이름입니다.")
else:
    print("잘못된 파일 이름입니다.")

s = "wwww.naver.com"
s = s.replace("com", "co.kr")       # "com" => "co.kr" 변환
print(s)

s = "www.naver.co.kr"
s = s.find(".kr")       # .kr이 시작되는 인덱스
print(s)

s = "Let it be, let it be, let it be"
s = s.rfind("let")      # let이 마지막에 등장하는 인덱스
print(s)

s = "www.naver.co.kr"
s = s.count(".")        # .이 등장하는 횟수
print(s)

# 문자 분류
"ABCabc".isalpha()

"123".isdigit()

"abc".islower()

"ABC".isupper()

# 공백 제거
s = " Hello, World!"
s.strip()           # 문자열의 첫부분 & 끝부분 공백 제거

s = "#######this is example######"
print(s.strip("#"))        # 특정문자 삭제

s = "#######this is example#######"
print(s.lstrip("#"))        # 왼쪽 끝, 원치않는 문자 삭제
print(s.rstrip("#"))        # 오른쪽 끝, 원치않는 문자 삭제

# 문자열 분해
s = "Welcome to Python"
print(s.split())                  # 인수가 없을 경우, 공백문자를 분리자로 가정하여 분해

s = "Hello, World!"
print(s.split(","))               # 인수(분리자) ","
print(s.split(", "))

print(list(s))                    # list()를 이용하여 모든 문자들로 분해하여 리스트로 반환

# 문자열 결합
joint = ", ".join(["apple", "grape", "banana"])         # 단어들 사이에 들어갈 문자(",") 지
print(joint)

phoneNum = "-".join("010.1234.5678".split("."))
print(phoneNum)


# Ch.5 함수
## 함수 작성 및 호출
def get_area(radius):
    area = 3.14*radius**2
    return area

result1 = get_area(3)
result2 = get_area(20)      # 서로 다른 인수로 호출할 수 있다.
print(f"반지름이 3인 원의 면적> {result1}")
print(f"반지름이 20인 원의 면적> {result2}")

# 여러 개의 값 반환
def get_input():
    return 2, 3

x, y = get_input()      # x=2, y=3

print(x, y)

# 함수 내에서는 아직 정의되지 않은 함수 호출 가능
def main():
    result3 = get_area1(3)
    print(f"반지름이 3인 원의 면적> {result3}")

def get_area1(radius):
    area = 3.14*radius**2
    return area

main()


# LAB
def main1():
    resultA = getPizzaArea(20) + getPizzaArea(20)
    resultB = getPizzaArea(30)
    print(f"20cm 피자 2개의 면적> {resultA} ")
    print(f"30cm 피자 1개의 면적> {resultB}")

def getPizzaArea(radius):
    if radius > 0 :
        area = 3.14*radius**2
    else:
        print("올바른 값을 입력하세요.")
    return area

main1();
