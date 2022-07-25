import math
# 소수 판별 함수
# 2이상의 자연수에 대해
def is_prime_number(x):
    # 2부터 x의 제곱근까지 모든 수를 확인하여 
    for i in range(2,int(math.sqrt(x))+1):
        #x가 해당하는 수로 나누어떨어진다면
        if x%1 ==0:
            return False
    return True


print(is_prime_number(4))

print(is_prime_number(7))