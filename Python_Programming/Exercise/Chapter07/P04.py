d = {x: x*10 for x in range(1, 7)}

findKey = int(input("키를 입력하시오> "))
# if d[findKey]:
if findKey in d:
    print(f'키 {findKey}는 딕셔너리 안에 있습니다.')
else:
    print(f'입력하신 키 {findKey}는 딕셔너리에 없습니다.')
