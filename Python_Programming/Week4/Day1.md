파이썬 프로그래밍 Week4 Day1
# 반복문

## 반복문 필요성
- 조건에 따라서 반복 실행 (특정조건에서 문장을 반복하여 실행)
- 반복적인 작업, 특히 **자동화**를 위해 필요함 (e.g. 에어컨 온도설정)
- 반복문 사용유무 비교
  ### 반복문을 사용하지 않는 경우
  ```
  print("방문을 환영합니다!");
  print("방문을 환영합니다!");
  print("방문을 환영합니다!");
  print("방문을 환영합니다!");
  print("방문을 환영합니다!");
  ```
  ### 반복문을 사용하는 경우
  ```
  for i in range(1000):
    print("방문을 환영합니다!");
  ```
- 반복의 종류
  - 횟수 반복(for문): 정해진 횟수만큼 반복 (e.g. 트랙을 10바퀴 뛰세요.)
    - 반복을 시작하기 전에 **반복의 횟수** 를 미리 아는 경우
  - 조건 반복(while문): 특정한 조건이 성립되는 동안 반복 (e.g. 기록이 1초 단축될 때까지 반복하세요.)
    - **특정한 조건이 만족**되는 동안 계속 반복

## FYI: 리스트
### Sequence type
 - 값이 연속적으로 이어진 자료형
 - e.g. 리스트, 튜플, range, etc.
### 리스트
- 파이썬의 데이터 구조 중 하나
- 여러 개의 자료를 모아서 하나의 묶음으로 저장
- 항목(item)들을 쉼표로 구분
- 대괄호 안에 항목들을 **순서대로** 작성
- 공백 생성 => 항목 추가
  - e.g. `list = []`
- 데이터 추가: append(), 리스트이름.append(데이터값)
  - e.g. `list.append(1)`
- 리스트 인덱스
  - 양수 인덱스: `0` 부터  시작
  - 음수 인덱스: `-1` 부터 시작
  - 예시
    ```
    slist = ["영어", "수학", "과학"]
    slist[0]
    slist[-1]
    ```
- 항목 변경
  - 아이템 변경
  - 예시
    ```
    slist = ["영어", "수학", "과학"]
    print(slist)
    slist[1] = "컴퓨터"
    print(slist)
    ```
## 횟수 제어 반복
### for문, foor loop
```
for 변수 in 리스트:
  문장1
  문장2
```
### range()
- 함수
- 반복횟수를 전달하면서, 자동으로 순차적인 정수들을 생성
```
for 변수 in range(종료값):
  문장1
  문장2
```
```
range(start = 0, stop, step=1)
# start: 시작값, stop: 종료값, stop: 종료값(stop은 포함X), step=1: 한 번에 증가되는 값
```
## 조건제어 반복
### While문
- 주어진(특정, 지정된) 조건이 만족되는 동안 반복
```
while 조건식:
  문장1
  문장2
```
- "while" with "else"
