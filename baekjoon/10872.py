# 재귀함수_팩토리얼
# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성
# 첫째 줄에 N!을 출력한다.

N = int(input())

def factorial(N):
    if N == 1 or N == 0:
        return 1
    return N * factorial(N-1)
print(factorial(N))