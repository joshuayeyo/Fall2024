# page 124
## 초등학생을 위한 산 퀴즈 프로그램
import random

x = random.randint(1,100)
y = random.randint(1,100)

answer = x + y

userInput = int(input(f'정답을 입력하세요: {x} + {y}> '))

if (userInput != answer):
    print(f'오답입니다!\n정답은 {answer}입니다.')
else:
    print("정답입니다!")