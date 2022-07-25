# 수학2
# 소수 찾기
# 주어진 수 소수가 몇개인지 찾아서 출력하세요.

# 입력 : 첫줄에 수의 개수 N이 주어진다.
# N <= 100
# 다음으로는 N개의 수가 주어지는데 수는 1000 이하의 수

# 출력 : 주어진 수들 중 소수의 개수를 출력
import sys
import math

n = int(input())
data = map(int, input().split())
count = 0

#data = list(map(int,sys.stdin.readline().split()))

def is_prime_number(x):
    # 2부터 (x-1)가지의 모든 수를 확인하여
    for i in range(2,x):
        #x가 해당하는는 수로 나누어떨어지면
        if x % i ==0:
            return False #소수가 아님
    return True #소수임


for i in data:
    if i > 1:
        if is_prime_number(i) == True:
            #print(i)
            count += 1
            
print(count)
