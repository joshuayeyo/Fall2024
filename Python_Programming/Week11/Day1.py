# 정보은닉 (Information hiding)
## __변수 이름 정의 (CAUTION: double underscore.)
class Student:
	def __init__(self, name=None, age=0):
		self.__name = name
		self.__age = age
obj = Student()
print(obj.__age)

## 인스턴스 변수 접근(메소드)
class Student1:
    def __init__(self, name=None, age=0):
        self.__name = name
        self.__age = age

    def getAge(self):
        return self.__age

    def getName(self):
        return self.__name

    def setAge(self, age):
        self.__age = age

    def setName(self, name):
        self.__name=name

obj=Student1("Hong", 20)
obj.getName()

## Lab: 은행계좌를 클래스로 모델링
### 현재잔액(balance)만을 인스턴스 변수로 함
### 생성자, 인출메소드(withdraw()), 저축메소드(deposit)

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def withdraw(self, amount):
        self.__balance -= amount
        print(f'통장에서 ${amount}가 출금되었음')
        return self.__balance
    def deposit(self, amount):
        self.__balance += amount
        print(f'통장에 ${amount}가 입금되었음')
        return self.__balance

a = BankAccount()
a.deposit(100)
a.withdraw(100)

# 8.5 객체 참조
## 함수를 통한 객체 변경

# 텔레비전을 클래스로 정의한다.
class Television:
    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on
    def show(self):
        print(self.channel, self.volume, self.on)

def setSilentMode(t):
    t.volume = 2
# setSilentMode()을 호출하여서 객체의 내용이 변경되는지 확인한다.
myTV = Television(11, 10, True);
setSilentMode(myTV)
myTV.show()

## 8.6 클래스 변수
class Monster:
    ### 상수 정의
    WEAK = 0
    NORMAL = 10
    STRONG = 20
    VERYSTRONG = 30

    def __init__(self):
        self.__health = Monster.NORMAL

    def eat(self):
        self.__health = Monster.STRONG

    def attack(self):
        self.__health = Monster.WEAK

### Lab: 강아지들의 품종이 같음 <= 강아지 객체마다 품종을 저장할 필요 없음
class Dog:
    kind = "Bulldog"        # 클래스 변수
    def __init__(self, name, age):
        self.name = name    # 각 인스턴스에 유일한 인스턴스 변수
        self.age = age      # 각 인스턴스에 유일한 인스턴스 변수
a = Dog("Baduk", 2)
b = Dog("Marry", 3)


print(a.kind)   # 모든 강아지가 공유
print(b.kind)   # 모든 강아지가 공유
print(Dog.kind) # 모든 강아지가 공유

print(a.name)   # 강아지 a에 유일
print(b.name)   # 강아지 b에 유일

## 8.7 특수메소드
class Circle:
    def __init__(self, radius):
        self.radius = radius

# __eq__ 메소드 주석처리하며 비교
    def __eq__(self, other):
        return self.radius == other.radius  # 반지름이 같은지를 비교

c1 = Circle(10)
c2 = Circle(10)

print(c1 == c2)     # (__eq__ 메소드) ? True : False

if c1 == c2:
	print("원의 반지름은 동일합니다.")    # __eq__ 메소드가 있다면 해당 statement 출력
else:
	print("원의 반지름은 상이합니다.")    # __eq__ 메소드가 없다면 해당 statement 출력

### Lab: 백터 객체에 특수 메소드 정의

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)
u = Vector2D(0, 1)
v = Vector2D(1, 0)
w = Vector2D(1, 1)
a = u + v
print(a)
