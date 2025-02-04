class Animal:
    def eat(self):
        print('먹는 중')


class Dog(Animal): #인자로=>상속의 기본표현
    def bark(self):
        print('멍멍')


my_dog = Dog()#인스턴스 생성

# 자식클래스(Dog) 인스턴스 호출
my_dog.bark()  #멍멍

# 부모 클래스(Animal) 메서드 사용 가능
my_dog.eat() #먹는 중