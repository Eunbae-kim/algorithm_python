# 1차원 array 평균
# 세준이는 기말고사를 망쳤다. 
# 세준이는 점수를 조작해서 집에 가져가기로 했다. 
# 일단 세준이는 자기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다. 
# 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.
# 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램

# 입력 : 
# 첫째 줄에 시험 본 과목의 개수 N (이 값은 1000보다 작거나 같다)
# 둘째 줄에 세준이의 현재 성적이 주어진다. 
# 이 값은 100보다 작거나 같은 음이 아닌 정수이고, 적어도 하나의 값은 0보다 크다.

# 출력 : 첫째 줄에 새로운 평균을 출력
N = int(input())
scores = list(map(int,input().split()))

max_score = max(scores)
new_scores = []

for i in range(len(scores)):
    new_scores.append(scores[i]/max_score*100)
average_score = sum(new_scores)/len(new_scores)
print(average_score)
