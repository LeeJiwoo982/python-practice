# 입출금이 가능한 은행 계좌 클래스 만들기
# 은행 계좌를 모델링하는 클래스를 만들고, 입출금 기능(메서드)를 구현


class BankAccount:
    interest_rate = 0.02  # 이자율

    def __init__(self, owner, balance=0): #두개의 인스턴스변수수
        self.owner = owner  # 계좌 소유자 # alice
        self.balance = balance  # 초기 잔액 #1000

    # 입금
    def deposit(self, amount):
        self.balance += amount # 1500
        # pass

    # 출금
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount #1300
        else:
            print('잔액 부족!\n>>그래서 출금진행 안된 것')
        # pass

    # 이자율 설정
    @classmethod
    def set_interest_rate(cls, rate):
        cls.interest_rate = rate
        # pass        

    # 금액이 양수인지 검증
    @staticmethod
    def is_positive(amount):
        return amount >0 # boolean 반환
        # pass

# 계좌 개설 (인스턴스 생성)
alice_acc = BankAccount('Alice', 1000)
print(f'계좌개설 시 잔액 확인:{alice_acc.balance}')

# 입금 및 출금 (인스턴스 메서드 호출)
alice_acc.deposit(500) #입급
print(f'입금 후 잔액:{alice_acc.balance}')

alice_acc.withdraw(3000) #출금

# 잔액 확인 (인스턴스 변수 참조)
print(f'출금 후 잔액:{alice_acc.balance}')

# 이자율 변경 (클래스 메서드 호출)
BankAccount.set_interest_rate(0.03)
print(f'이자율 변경확인:{BankAccount.interest_rate}')  # 0.03

# 잔액이 양수인지 확인 (정적 메서드 호출)
BankAccount.is_positive(alice_acc.balance)
print(f'잔액이 양수인지?:{BankAccount.is_positive(alice_acc.balance)}')  # True
