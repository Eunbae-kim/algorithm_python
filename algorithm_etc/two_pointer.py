# 투 포인터
# two pointer
# 특정합을 가지는 부분 연속 수열 찾기 : 문제 해결 아이디어

n = 5 #데이터 개수
m = 5 #찾고자 하는 부분합
data = [1,2,3,2,5] #전체 수열 초기화
count = 0

interval_sum = 0 # 현재 부분 수열값
end = 0

#start를 차례대로 증가시키며 반복
for start in range(n):
    # endㄹ르 가능한 만큼 이동시키기
    while interval_sum <m and end <n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count +=1
    interval_sum -= data[start]

print(count)