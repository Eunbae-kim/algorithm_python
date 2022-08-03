# 그리디알고리즘
# 1이 될 때까지

# 문제
# 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
# 단, 두번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다
  # N에서 1을 뺀다.
  # N을 K로 나눈다.

# 입력조건
# 첫번째 줄에 N, K가 공백으로 구분되어 자연수로 주어진다. 
# 이 때 입력으로 주어지는 N은 항상 K보다 크거나 같다. 

# 출력 
# 첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행하는 횟수의 최솟값을 출력한다.

n,k = map(int,input().split())
count =0

while True:
    if (n % k) == 0:
        n = (n//k)
        count += 1
        if n == 1:
            break
    else:
        n -= k
        count += 1
        if n == 1:
            break
print(count)
