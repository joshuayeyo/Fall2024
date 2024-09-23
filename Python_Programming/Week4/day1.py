from sre_constants import REPEAT_ONE


list = []       # 공백 리스트를 생성한다.
# 리스트에 데이터를 추가한다.
list.append(1)
list.append(2)
list.append(6)
list.append(3)

print(list)     # 리스트를 출력한다.

slist = ["영어", "수학", "과학"]
print(slist)
slist[1] = "컴퓨터"
print(slist)

for i in [1,2,3,4,5]:
    print(i,"번째 방문을 환영합니다.")

for i in [1, 2, 3, 4, 5]:
    print("count >", i)

for i in [1, 1, 1, 1, 1]:
    print("i = ", i)

for i in range(5):
    print("range 반복문입니다.", i, "회 반복하는 중")
# 간격지정
for i in range(1, 6, 1):
    print(i, end=" ")
print("")

# 역순
for i in range(10, 0, -1):
    print(i, end=" ")
print("")
# 1~n 까지의 합
sum = 0
n = 10
for i in range(1, n+1):
    sum += i
print("합 = ", sum)

# 구구단 출력
for i in range(1, 6):
    print("9 *", i, "=", 9*i)

# While문 예제
TARGET = 2000
money = 1000
year = 0
interest = 0.07
# 현재 금액이 목표 금액보다 작으면 반복합니다.
while money < TARGET :
    money = money + money * interest
    year += 1
print(year, "년 뒤에 목표금액을 달성합니다.")

# ex) 1과 10까지의 합 계산하기 (p.174)
i = 1   # 제어변수 선언
sum = 0
# i 값이 10보다 작거나 같으면 반복
while i <= 10 :
    sum = sum + 1
    i+=1
print("합계는", sum)

# "while" with "else"
i = 0
while i < 3:
    print("루프 안쪽")
    i+=1
else:
    print("else 부분")
