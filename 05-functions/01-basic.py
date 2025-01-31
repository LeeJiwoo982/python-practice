# 두 수의 합을 구하는 코드
num1 = 5
num2 = 3
sum_result = num1 + num2
print(sum_result)

# 두 수의 합을 구하는 함수
def get_sum(num1, num2):
    return num1+num2

# 함수를 호출하여 결과 출력
sum_result = get_sum(num1, num2)
print(sum_result)


def make_sum(pram1, pram2): # (pram1,pram2)=몇개의 값을 받을지.=parameter=INPUT
    """
    이것은 두 수를 받아
    두 수의 합을 반환하는 함수입니다.
    >>> make_sum(1, 2)
    3
    """ #도큐먼트 스트릿, Docstring=이 함수에 대한 설명서
    return pram1 + pram2 #(""" ~ return)=함수의 바디=function body, #return value=output=f(x)

# 함수 호출
result = make_sum(100, 50)
print(result)


# 함수와 반환 값
# print() 함수는 반환값이 없다.

return_value = print(1)
print(return_value) # None >> 반환값이 없음을 증명

# 출력과 반환은 다르다. 화면에 출력을 하는 코드가 작성됨.

def my_func():
    print('hello')
    return None

result = my_func()
print(result)