class Person:
    name = 'unknown'

    def talk(self):
        print(self.name)


p1 = Person() #변수설정 안함
p1.talk()  # unknown

# p2 인스턴스 변수 설정 전/후
p2 = Person()
p2.talk()  # unknown
p2.name = 'Kim'
p2.talk()  # Kim # 클래스변수는 바뀐게 아님. p2에 할당한 것ㄹ

print(Person.name)  # unknown
print(p1.name)  # unknown
print(p2.name)  # Kim
