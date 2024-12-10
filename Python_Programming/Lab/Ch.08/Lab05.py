# page 391 클래스 변수 예제

class Dog:
    kind = "Bulldog"
    def __init__(self, name, age):
        self.name = name
        self.age = age

a = Dog("Baduk", 2)
b = Dog("Marry", 3)

print("Baduk의 품종은", a.kind)
print("Marry의 품종은", b.kind)

print(a.name)
print(b.name)
