# 수학 2
# 더 빠르게 소수 구하기
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다.

# 출력 : 한 줄에 하나씩, 증가하는 순서대로 소수를 출력

x, y = map(int, input().split())

for i in range(x, y+1):
    if i == 1: #1은 소수가 아뉘지!
        continue
    for j in range(2, int(i** 0.5)+1 ):
        if i%j==0:
            break
    else:
        print(i)


