# page 278
## 리스트 슬라이싱

numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

reversedList = numList[::-2]
print(reversedList)

## 리스트 슬라이싱만 이용하여 첫 번째 요소만을 남기고 전부 삭제할 수 있는가?
numList[1:] = []

print(f'{numList}')
