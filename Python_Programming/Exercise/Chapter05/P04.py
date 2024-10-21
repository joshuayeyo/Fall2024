# 90점 이상이면 A, 80점 이상이면 B, 70점 이상이면 C, 60점 이상이면 D, 그외에는 F를 반환하는 함수 getGrade(score)을 작성하고 테스트하여라.
def getGrade(score):
    if (score >= 90):
        print("A")
    elif (score >= 80):
        print("B")
    elif (score >= 70):
        print("C")
    elif (score >= 60):
        print("D")
    else:
        print("F")


score = int(input("성적을 입력하세요> "))
getGrade(score)
