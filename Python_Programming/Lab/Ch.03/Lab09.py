# page 143
## 축구게임

import random

computerChoice = random.randint(1, 3)

userChoice = int(input("수비할 곳을 선하세요.\n1. 왼쪽\n2. 중앙\n3. 오른쪽\n> "))

if (computerChoice == userChoice):
    print("수비에 성공하셨습니다.")
else:
    print("컴퓨터가 골을 넣었습니다.")