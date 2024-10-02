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

fruits[1] = "pear"      # 오류 발
