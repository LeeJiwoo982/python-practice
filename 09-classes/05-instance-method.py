class Counter:
    def __init__(self): # 큰 범주에서는 인스턴스 메서드
        self.count = 0
    
    def increament(self):
        self.count += 1


c = Counter()
c.increament()

# Counter.__init__(인스턴스)

print(c.count) # 0

c2 = Counter()
c.increament()
print(c2.count)