# 조건문 _ 알람시계
# 원래 설정되어 있는 알람을 45분 앞서는 시간으로 바꾸는 것

# 입력 : 
# 첫째 줄에 두 정수 H와 M이 주어진다. (0 ≤ H ≤ 23, 0 ≤ M ≤ 59) 
# 알람 시간 H시 M분을 의미

# 출력 : 
# 첫째 줄에 상근이가 창영이의 방법을 사용할 때, 설정해야 하는 알람 시간을 출력한다.
# (입력과 같은 형태로 출력하면 된다.)

H,M = map(int, input().split())
if M>=45:
    print(H, M-45)
elif M < 45 and H==0:
    print('23', 60+(M-45))
else:
    print(H-1, 60+(M-45))