# page 265
## 성적 처리 프로그램

numStudents = int(input("학생의 수를 입력하세요> "))      # 내가 추가한 구문
lScores = []
count = 0

for i in range(numStudents):
    score = int(input("성적을 입력하시오> "))

    lScores.append(score)

for score in lScores:
    if score >= 80:
        count+=1

averageScore = sum(lScores)/numStudents


print(f'성적 평균 = {averageScore}')
print(f'최대점수 = {max(lScores)}')
print(f'최소점수 = {min(lScores)}')
print(f'80점 이상 = {count}명')
