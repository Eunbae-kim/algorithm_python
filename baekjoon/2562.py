# 1 차원 배열 _ 최댓값
# 9개의 서로 다른 자연수가 주어질 때, 
# 이들 중 최댓값을 찾고 
# 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

# 입력 : 
# 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 
# 주어지는 자연수는 100 보다 작다.

# 출력 : 
# 첫째 줄에 최댓값을 출력하고, 
# 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.

alist = []

for i in range(9):
    alist.append(int(input()))

alist_max = alist[0]
alist_index = 0

for j in range(9):
    if alist[j] >= alist_max:
        alist_max = alist[j]
        alist_index = j + 1

print(alist_max)
print(alist_index)