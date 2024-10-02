# 튜플
## 요소가 1개 있을 때
single_tuple = ("apple", )      # 쉼표가 끝에 있어야 함.
print(single_tuple)

no_tuple = ("apple")
print(no_tuple)

## 변경 불가능
fruits = ("apple", "banana", "grape")
fruits[1]
print(fruits)

# fruits[1] = "pear"      # 오류 발

## 튜플생성(변환)
myList = [1, 2, 3, 4]
myTuple = tuple(myList)
print(myTuple)

## 리스트생성(변환)
myTuple = (1, 2, 3, 4)
myList = list(myTuple)
print(myList)

## 튜플 연산
### 추가
fruits += ("pear", "kiwi")
print(fruits)

numbers = [10, 20, 30]
numbers += (40, 50)
print(numbers)

## 패킹과 언패킹
n1 = 10
n2 = 90
n1, n2 = (n2, n1)

## enumerate()
fruits = ["apple", "banana", "grape"]
for index, value in enumerate(fruits):
    print(index, value, end=" ")
print("\n")

# Set
## List => Set
numbers = set([1,2,3,1,2,3])
print(numbers)

letters = set("abc")
print(letters)
