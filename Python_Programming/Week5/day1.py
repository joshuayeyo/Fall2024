heroes = []
heroes.append("아이언맨")
heroes.append("토르")
print(heroes)

# built-in function
numbers = [10, 20, 30, 40, 50]
print("합=", sum(numbers))        # 항목의 합계를 계산한다.
print("최대값=", max(numbers))     # 가장 큰 항목을 반환한다.
print("최소값=", min(numbers))     # 가장 작은 항목을 반환한다.

# 랜덤으로 선택하기
import random

numList = [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10]
print("랜덤하게 선택한 항목=", random.choice(numList))

# 리스트 합병
heroes1 = ["아이언맨", "토르"]
heroes2 = ["헐크", "스칼렛 워치"]
avengers = heroes1 + heroes2

print(avengers)

# 리스트 복제
nums = [1, 2, 3, 4]
newNums = [1, 2, 3, 4] * 3
print(newNums)

# 리스트 비교
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)       # True

list3 = [3, 4, 5]
list4 = [1, 2, 3]
print(list1 > list2)        #False

# 리스트 복사
temps = [28, 31, 33, 35, 27, 26, 25]
values1 = temps

print(temps)
values1[3] = 39
print(temps)
print(values1)

# list()
print("list()로 리스트 생성해보자")
tmps = [28, 31, 33, 35, 27, 26, 25]
values2 = list(tmps)

print(tmps)
values2[3] = 39
print(tmps)
print(values2)

# 슬라이싱
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# numbers[:3]
print(numbers[:3])  # [10, 20, 30]
# numbers[3:]
print(numbers[3:])  # [40, 50, 60, 70, 80, 90]
# numbers[:]
print(numbers[:])   # [10, 20, 30, 40, 50, 60, 70, 80, 90]

new_numbers= numbers[:]

# 간격을 주고 잘라내기 (list[ start : stop : step])
numbers[2:7:2]
