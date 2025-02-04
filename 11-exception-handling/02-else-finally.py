try:
    x = int(input('숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('유효한 숫자가 아닙니다.')
else: # except 실행 안할 때
    print(f'결과: {y}')
finally: # 모든 것의 마지막
    print('프로그램이 종료되었습니다.')
