n = int(input())
data = list(map(int, input().split()))
data.sort() #오름차순으로 공포도 정렬

result = 0 # 총 그룹의 갯수
count = 0 # 현재 그룹에 포험된 모험가의 수

for i in data: # 공포도가 낮은 것부터 하나씩 확인하면서
    count+= 1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹을 결성함
        result += 1 #그룹이 하나 증가
        count = 0 # 이제 새로운 그룹 짜야 되니까 혀냊 그룹에 포함된 모험가의 수 0으로
print(result)