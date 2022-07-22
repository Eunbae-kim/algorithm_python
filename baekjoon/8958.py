# # 1차원 배열 OX퀴즈
# # O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 
# # 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다.

# # 입력 : 
# # 첫째 줄에 테스트 케이스의 개수가 주어진다.
# # 각 테스트 케이스는 한 줄로 이루어져 있고, 
# # 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 
# # 문자열은 O와 X만으로 이루어져 있다.

# # 출력 : 각 테스트 케이스마다 점수

# N = int(input())
# lists = []
# n_scores = []
# for i in range(N):
#     lists.append(list(input()))

# for j in range(N):
#     alist = lists[j]
#     print(alist)
#     print(len(alist))
#     scores = [0]*len(alist)
#     for i in range(len(alist)):
        
#         if alist[i] == 'X':
#             scores[i] = 0
#         else:
            
#             if i != 0:
#                 if alist[i-1] == 'O':
#                     scores[i] += 1
#             if i == len(alist)-1:
#                 # scores[i] += 1
#                 break
#             else:
#                 scores[i+1] += 1
#     print(scores)
#     print(sum(scores))
 
N = int(input())

for i in range(N):
    a = input()
    score = 0
    sumScore = 0
    for j in a:
        if j == 'O':
            score += 1
        else:
            score = 0
        sumScore += score
    print(sumScore)