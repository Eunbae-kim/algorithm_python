# 접두사 합
# 구간 합빠르게 구ㅏ기

#데이터 개수 N과 데이터 입력받기
n = 5
data=[10,20,30,40,50]

# 접두사 합 배열 계산
# Prefix Sum
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value +=i
    prefix_sum.append(sum_value)

# 구간 합 계산
# 세번째 수부터 네 번쨰 수까지
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left-1])