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

## 연산
fruits = {"apple", "banana", "grape"}
size = len(fruits)
print(size)

if "apple" in fruits:
    print("집합 안에 apple이 있습니다.")
else:
    print("집합 안에 apple이 없습니다.")

for x in fruits:            # 순서 없음(무작위)
    print(x, end=" ")
print("\n")
for x in sorted(fruits):
    print(x, end=" ")
print("\n")

## 함축연산, [] vs. {}
aList = [1, 2, 3, 4, 5, 1, 2]
result = { x for x in aList if x%2==0 }
print(result)

## 부분집합 연산
A = {"apple", "banana", "grape"}
B = {"apple", "banana", "grape", "kiwi"}
if A.issubset(B) :
    print("A는 B의 부분집합입니다.")

## 비교
if A == B:
    print("A는 B와 같습니다.")
else:
    print("A는 B와 같지 않습니다.")

# 딕셔너리
## 항목 탐색
capitals = {"Korea": "Seoul", "America": "Washington", "France": "Paris"}
print(capitals["Korea"])

# print(capitals["Japan"])  # 에러 발
print(capitals.get("Japan", "해당 키가 없습니다."))

## 항목 추가
# capitals = {}
# capitals["Korea"]="Seoul"
capitals["China"]="Beijing"
capitals["Japan"]="Tokyo"

print(capitals)

city = capitals.pop("France")
if "France" in capitals:
    capitals.pop("France")
print(capitals)
print(city)
if "France" in capitals:
    del_city = capitals.pop("France")
