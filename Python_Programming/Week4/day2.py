# # 무한루프의 예
# i = 0
# # 변수 i를 증가시키는 부분이 없어서 무한루프가 된다.
# while i < 10:
#     print("Hello!");

# 중첩 반복문
# (p.182)
for y in range(5) :
    for x in range(10) :
        print("*", end="")
    print("") # 줄바꿈 문자

# (p.183)
for y in range(1, 6) :
    for x in range(y) :
        print("*", end="")
    print("") # 줄바꿈 문자

# (p.183) 모든 조합 구하기
adj = ["small", "medium", "large"]
nouns = ["apple", "banana", "grape"]
for x in adj:
    for y in nouns:
        print(x,y)

# 무한루프와 Brake, Continue
# p.186
while True:
    light = input("신호등 색상을 입력하세요>")
    if light == 'green':
        break

print("건너가도 좋습니다.")

# (p.187)
for i in range(1, 11):
    if i %3 == 0:
        continue  # 3의 배수이면 다음 반복을 시작한다.
    print(i, end=" ")

# 리스트
# index 연산
print("")
heroes = ["아이언맨", "토르", "헐크", "스칼렛 위치", "헐크"]
n = heroes.index("헐크")
print(n)        # 헐크가 2가 되는 까닭은?

heroes = ["아이언맨", "토르", "헐크", "스칼렛 위치", "헐크"]
if "헐크" in heroes:
    print(heroes.index("헐크"))
n = heroes.index("헐크", 3)

heroes = ["아이언맨", "토르", "헐크", "스칼렛 위치", "헐크"]
if "헐크" in heroes:
    a = heroes.index("헐크")
    n = heroes.index("헐크", a+1)
print(n)
