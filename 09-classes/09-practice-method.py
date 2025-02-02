# 입출금이 가능한 은행 계좌 클래스 만들기
# 은행 계좌를 모델링하는 클래스를 만들고, 입출금 기능(메서드)를 구현


class BankAccount:
    interest_rate = 0.02  # 이자율

    def __init__(self, owner, balance=0):
        self.owner = owner  # 계좌 소유자
        self.balance = balance  # 초기 잔액

    # 입금
    def deposit():
        pass

    # 출금
    def withdraw():
        pass

    # 이자율 설정
    @classmethod
    def set_interest_rate():
        pass

    # 금액이 양수인지 검증
    @staticmethod
    def is_positive():
        pass


# 계좌 개설 (인스턴스 생성)


# 입금 및 출금 (인스턴스 메서드 호출)


# 잔액 확인 (인스턴스 변수 참조)


# 이자율 변경 (클래스 메서드 호출)
print()  # 0.03

# 잔액이 양수인지 확인 (정적 메서드 호출)
print()  # True
