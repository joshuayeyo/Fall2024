# CHAPTER.04
## 중첩 반복문
## 반복루프 in 반복루프 
```
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

```

## 무한루프와 Break, Continue
- 필요에 의한 무한루프 사용 시,


## Lab
p.168, 170, 176, 179, 184, 187


# CHAPTER.06: 파이썬 자료구조1 (리스트)
## 리스트 개요
### 리스트
- 항목들을 저장하는 컨테이너(공간)으로서 그 안에 항목들이 순서를 갖고 저장됨
## 리스트 조회
```
temps = [28, 31, 33, 35, 27, 26, 25]
for element in temps:
print(element, end=", ")
```
- zip() : 2개의 리스트를 받아서 항목 2개를 묶음으로 제공
	```
	questions = ['name', 'quest', 'color']
	answers = ['Kim', 'Python', 'blue]
	for q, a in zip(questions, answers): 
		print(f"What is your {q?} it is {a}")
	```
	

### 리스트 길이 len() 
- range(len(temps)) : 0~ 리스트의 길이 - 1
```
temps = [28, 31, 33, 35, 27, 26, 25]
for i in range(len(temps)):
	print(temps[i], end=', ')
```

## 리스트 연산들
### append()
	- 공백 생성 => 항목 추가
	- 리스트에 몇 개의 항목이 들어갈 지 예측 불가한 경우
		```
		heroes = []
		heroes.append("아이언맨")
		heroes.append("토르")
		print(heroes)
		```
### insert()
	- 새로운 아이템 삽입
	- 인덱스: 0 ~ 요소 수
### index()
	- 리스트 탐색, 리스트이름.index(요소)
	- `n=heroes.index("아이언맨")` : n은 해당 item의 {index}가 된다.
### 요소 삭제
	- pop(i): 항목이 저장된 위치를 알고 있다면,
	- remove(value): 항목의 값만 알고 있다면
### 최대, 최솟값
- 최소값, min()
- 최대값, max()
### 정렬 1
- sort() : 크기순으로 정렬, 원본리스트 변경
	- cf) 역순: sort(reverse=True)
- sorted(): 크기순으로 정렬, 새로운 리스트 생성 (원본리스트 유지)
	```
	list = [3, 2, 1]
	new_list = sorted(list)
	print(nList)
	```
- Method
	- 메소드는 특정 객체에 속한 함수
	- 해당 객체의 상태나 동작을 변경하거나 조회하는 역할
	- 메소드는 항상 객체와 연결되어 사용되며, 객체에 대한 작업을 수행