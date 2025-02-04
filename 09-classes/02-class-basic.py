class Person:
    def __init__(self, name, age): # 생성자 매서드
        self.name = name  # 인스턴스 속성
        self.age = age  # 인스턴스 속성

    def introduce(self): # 실제 매서드
        print(f'안녕하세요. 저는 {self.name}, 나이는 {self.age}살입니다.')
