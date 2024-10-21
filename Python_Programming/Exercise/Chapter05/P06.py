#사용자로부터 2개의 정수를 받아서 수학 문제를 만들어 화면에 출력하는 함수를 작성하고 테스트하시오.

def generateProblems(firstInput, secondInput):
    problem = firstInput + secondInput
    print(problem)

firstInput = int(input("첫 번째 정수를 입력하시오> "))
secondInput = int(input("두 번째 정수를 입력하시오> "))
generateProblems(firstInput, secondInput)
