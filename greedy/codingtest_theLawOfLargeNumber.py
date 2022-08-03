# 이것이 코딩테스트다_그리디
# 큰 수의 법칙
# 동빈이이 큰수의 법칙은 다양한 수로 이루어진 배열이 있을 때 
# 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
# 단 배열의 특정 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.

# 입력조건
# 첫번째 줄에 N, M,K 자연수가 주어지며 각 자연수는 공백으로 구분
# 둘 째 줄에 N개의 자연수가 주어진다
# K는 늘 M보다 작거나 같다

# 출력 조건
# 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다.

N, M, K = map(int, input().split())
n_list = list(map(int, input().split()))

n_list_sort = sorted(n_list,reverse=True)

result = 0
i= 2
max = n_list_sort[0]
second = n_list_sort[1]

while M >= 0:
    if M >= K:
        if (i%2) == 0:
            result += max*K
            M -= K
            i += 1
        else:
            result += second
            M -= 1
            i += 1
    else:
        if (i%2) == 0:
            result += max*M
            break
        else:
            result += second 
            M -= 1
            result += max*M
            break
print(result)       

    






