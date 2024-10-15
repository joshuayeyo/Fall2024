# page 142
## 사용자 입력 검증하기

print("===============")
print("메뉴 1번: 치즈 버거\n메뉴 2번: 치킨 버거\n메뉴 3번: 불고기 버거")
print("===============")

userChoice = int(input("주문할 메뉴 번호를 입력하세요> "))

if (1 <= userChoice and userChoice <=3):
    print(f'메뉴: {userChoice}')
else: 
    print("잘못 입력하셨습니다.")