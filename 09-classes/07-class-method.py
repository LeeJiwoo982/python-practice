class Person:
    population = 0 # 클래스변수는 맨 위쪽에 다 써두고 아래에 메서드 정의한다.

    def __init__(self, name):
        self.name = name
        Person.increase_population() # *클래스메서드 호출*은 "클래스"가 한다
    
    @classmethod # 클래스를 꾸며준다다
    def increase_population(cls): # 첫번째 인자로 클래스자기자신이 들어간다다
        cls.population += 1 # 클래스 변수를 하나 씩 늘리겠다. 생성될 때마다 자동 호출


person1 = Person('Alice')
person2 = Person('Bob')
print(Person.population)  #2