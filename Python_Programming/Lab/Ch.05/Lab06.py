# page 285
## 누적값 리스트 만들기

list1 = [10, 20, 30, 40, 50]
list2 = [sum(list1[0:x+1]) for x in range(0, len(list1))]

print(list2)
