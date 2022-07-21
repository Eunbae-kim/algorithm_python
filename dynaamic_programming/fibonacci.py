# 피보나치 함수 Fibonacci Function을 재귀함수로 구현
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(1))
print(fibo(2))
print(fibo(3))
print(fibo(4)) 
print(fibo(5))
print(fibo(6))