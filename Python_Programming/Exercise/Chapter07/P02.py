# (x, x*x)형식의 숫자 (1과 10사이)를 포함하는 딕셔너리를 생성하고 출력하는 프로그램을 작성해보자.

dict = {x:x*x for x in range(1, 11)}        # 딕셔너리 함축에서 colon이 빠지면 set을 생성하는 함축이 된다.

print(dict)
