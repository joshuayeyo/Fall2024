# 2개의 정수를 크기 순으로 반환하는 함수 getSorted(x, y)를 작성하고 테스트하라. 파이썬의 다중값 반환하기 기능을 사용하자.



def getSorted(firstInput, secondInput):
    if (firstInput > secondInput):
        bigger = firstInput
        smaller = secondInput
    elif (firstInput < secondInput):
        bigger =secondInput
        smaller = firstInput
    else:
        return 1;   # 2개의 값이 아닌 하나의 값만 반환하고 있기 때문에 오류가 발생.

    return bigger, smaller


def main():
    firstInput = int(input("첫 번째 정수> "))
    secondInput = int(input("두 번째 정수> "))

    bigger, smaller = getSorted(firstInput, secondInput)
    print(bigger, smaller)

main()
