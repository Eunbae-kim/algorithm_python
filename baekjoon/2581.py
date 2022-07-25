# 수학 2
# 소수
# 자연수 M과 N이 주어질 때
# M이상 N이하의 자연수 중 소수인 것을 모두 골라 
# 이들 소수의 합과 최솟값을 찾는 프로그램

# 입력 : 
# 입력의 첫째 줄에 M이, 둘째 줄에 N

# 출력 : M이상 N이하의 자연수 중 소수인 것을 모두 찾아 
# 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력
# M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1

def is_prime_number(x):
    if x == 1:
        return False
    # 2부터 (x-1)가지의 모든 수를 확인하여
    for i in range(2,x):
        #x가 해당하는는 수로 나누어떨어지면
        if x % i ==0:
            return False #소수가 아님
    return True #소수임

M = int(input())
N = int(input())

length = N - M + 1

prime = []

for i in range(M,N+1):
    if is_prime_number(i):
        prime.append(i)


if (len(prime)>0):
    print(sum(prime))
    print(min(prime))
else:
    print(-1)
