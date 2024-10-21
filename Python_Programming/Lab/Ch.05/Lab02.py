# page 266
## 리스트에서 2번째 큰 수 찾기

list = [1, 2, 3, 4, 15, 99]

# case1: 가장 큰 수를 지운 뒤 출력한다.
list.remove(max(list))

print(f'리스트에서 2번째로 큰 수는 {max(list)}')

# case2: 리스트를 정렬한 뒤 2번째로 큰 수를 뽑아낸다.

list = [1, 2, 3, 4, 15, 99]

list.sort()
print(f'리스트에서  2번쨰로 큰 수는 {list[-2]}')       ## 2번째 말고 3번째, 4번째 등 유동적으로 재사용이 가능하기에 2번째 방식이 더 좋은 것 같다.
