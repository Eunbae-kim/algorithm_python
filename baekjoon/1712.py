# 손익분기점
# 월드전자는 노트북을 제조하고 판매하는 회사이다. 
# 노트북 판매 대수에 상관없이 매년 임대료, 재산세, 보험료, 급여 등 A만원의 고정 비용이 들며, 
# 한 대의 노트북을 생산하는 데에는 재료비와 인건비 등 총 B만원의 가변 비용이 든다

# 입력 : 
# 첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다.
#  A, B, C는 21억 이하의 자연수이다

# 출력 :
# 첫 번째 줄에 손익분기점 즉 최초로 이익이 발생하는 판매량을 출력한다. 
# 손익분기점이 존재하지 않으면 -1을 출력
A,B,C = map(int, input().split())
n = 1
while True:
    if B >= C:
        n = -1
        break
    if (A + B*n) < C*n:
        break
    else:
        n += 1

print(n)
