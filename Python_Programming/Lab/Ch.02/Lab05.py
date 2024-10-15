# page 105
## BMI 계산하기
weight = float(input("몸무게를 kg 단위로 입력하세요> "))
height = float(input("키를 미터단위로 입력하세요> "))

BMI = weight/height**2

print(f'당신의 BMI={BMI}')