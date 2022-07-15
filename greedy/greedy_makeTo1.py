#n, k를 공백을 기준으로 입력받음
n, k = map(int, input().split())

#N과 K가 주어질 떄 N이 1이 될 때 까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수 : result
result = 0

while True:
    while n%k == 0:
        n=n // k
        result += 1
    if n == 1:
        break
    n -= 1
    result+=1

print(result)