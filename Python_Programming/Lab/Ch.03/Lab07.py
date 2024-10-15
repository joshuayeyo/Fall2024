# page 141
## 8 매직볼
import random

print("행운의 매직볼로 오늘의 운세를 출력합니다.")
magicBall = random.randint(1, 8)

if (magicBall == 1):
    print("확실히 이루어집니다.")
elif (magicBall == 2):
    print("좋아 보이네요.")
elif (magicBall == 3):
    print("믿으셔도 됩니다.")
elif (magicBall == 4):
    print("저의 생각에는 no입니다.")
else:
    print("다시 질문해주세요.")
