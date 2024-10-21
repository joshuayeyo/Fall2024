# page 269
## 친구관리 프로그램

choice = 0
friends = []

while choice != 9:
    print("-----------------")
    print("1. 친구 리스트 출력")
    print("2. 친구추가")
    print("3. 친구삭제")
    print("4. 이름변경")
    print("9. 종료")
    print("-----------------")
    choice = int(input("메뉴를 선택하시오> "))

    if (choice == 1):
        print(f'1번 메뉴입니다.\n{friends}')
    elif (choice == 2):
        print("2번 메뉴입니다.")
        name = str(input("이름을 입력하시오> "))
        friends.append(name)
    elif (choice == 3):
        print("3번 메뉴입니다.")
        name = str(input("이름을 입력하시오> "))
        friends.remove(name)
    elif (choice == 4):
        print("4번 메뉴입니다.")
        old_name = str(input("변경할 이름을 입력하시오> "))
        if old_name in friends:
            i = friends.index(old_name)
            new_name = str(input("변경할 이름을 입력하시오> "))
            friends[i] = new_name
            print(f'{old_name}이(가) {new_name}으로 변경되었습니다.')
        else:
            print("이름이 없습니다.")
            break
    elif (choice == 9):
        print("종료됩니다.")
