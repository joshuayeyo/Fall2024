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

# 역순으로 만들기
print(numbers[::-1])

# 리스트 일부 변경
lst1 = [1, 2, 3, 4, 5, 6, 7, 8]
lst1[0:3] = ['white', 'blue', 'red']
print(lst1)

# 리스트 중간 변경
lst2 = [1, 2, 3, 4, 5, 6, 7, 8]
lst2[::2] = [99, 99, 99, 99]
print(lst2)

# 리스트 모든 요소 삭제
lst3 = [1, 2, 3, 4, 5, 6, 7, 8]
lst3[:] = []
print(lst3)

# 리스트 특정요소 삭제
numbers = list(range(0, 10))    # 0에서 시작하여 9까지를 저장하는 리스트
print(numbers)
del numbers[-1]                 #마지막 항목을 삭제한다.
print(numbers)

# 문자열과 리스트
s = "Monthy Python"
print(s[0])
print(s[6:10])
print(s[-12:-7])

# 리스트 함축
sqrs = []
for x in range(10):
    sqrs.append(x*x)
print(sqrs)

sqrs1 = [ x*x for x in range(10)]
print(sqrs1)

# if문을 추가하여 '조건 추가'
sqrs2 = []
for x in range(10):
    if x % 2 == 0:
        sqrs2.append(x*x)
print(sqrs2)

prices = [135, -545, 922, 356, -992, 217]
mprices = [i if i >0 else 0 for i in prices]
print(mprices)

words = ["All", "good", "things", "must", "come", "to", "an", "end."]
letters = [w[0] for w in words]
print(letters)

numbers = [x+y for x in ['a','b','c'] for y in ['x','y','z']]
print(numbers)

# 2차원 리스트
s = [
    [ 1, 2, 3, 4, 5 ],
    [ 6, 7, 8, 9, 10 ],
    [ 11, 12, 13, 14, 15 ]
]

print(s)

# 2차원 리스트의 동적생성
rows = 3
cols = 5
s = []
for row in range(rows):
    s += [[0]*cols] # 2차원 리스트끼리 합쳐진다.
    s += [0*cols]   # 1차원 리스트끼리 합쳐진다.
print("s =", s)

# 리스트 함축 이용
rows = 3
cols = 5
s = [ (0 * cols) for row in range(rows)]
print("s =", s)
