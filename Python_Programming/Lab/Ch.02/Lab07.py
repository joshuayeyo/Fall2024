# page 107
## 자동판매기 프로그램
price = int(input("물건값을 입력하시오> "))
print("=== 입력금액 ===")
sen = int(input("1000원 지폐 개수> "))
gohyaku = int(input("500원 동전 개수> "))
hyaku = int(input("100원 동전 개수> "))

change = sen*1000 + gohyaku*500 + hyaku*100 - price
print(f'거스름돈은 {change}원 입니다.')

nGohyaku = change//500
change = change%500

nHyaku = change//100
change = change%100

nJyuu = change//10
change = change%10

nIchi = change

print(f'500원= {nGohyaku} 100원= {nHyaku} 10원= {nJyuu} 1원= {nIchi}')