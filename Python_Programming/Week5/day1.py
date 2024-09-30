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
