# set1, set2 2개의 세트가 주어져 있다고 하자. set1 또는 set2, 어느 한쪽에만 있고 요소들을 출력하는 프로그램을 작성하라.

set1 = {10, 20, 30, 40, 50, 60}
set2 = {30, 40, 50, 60, 70, 80}
intersection = set1 & set2
print(intersection)

answer = (set1.difference(intersection) | set2.difference(intersection))

print(f'어느 한쪽에만 있는 요소들 {answer}')
