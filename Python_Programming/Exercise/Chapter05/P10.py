# 주어진 정수가 소수인지를 검사하는 testPrime(n)을 작성하고 이 함수를 호출하여 2부터 100 사이의 소수를 출력하여 보자.

def testPrime(n):
    prime = True
    dividor = 2
    while (dividor < n):
        if (n%dividor) == 0:    # 나머지가 없는 경우
            prime = False
            break
        dividor += 1

    if n == 2:                  # 2는 소수이지만, 2%2 == 0 이기에 이렇게 처리 해줘야 함.
        prime = True

    if prime == True:           # 나머지가 있는 경우, 콘솔에 출력한다.
        print(n, end=" ")


for num in range(2, 101):
    testPrime(num)
