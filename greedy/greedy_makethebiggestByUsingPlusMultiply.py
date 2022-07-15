#먼저 숫자로만 이루어진 문자열 S를 입력받음
data = input()

#첫번재 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1,len(data)):
    # 두 수 중에서 하나라도 0 혹은 1인 경우 곱하기 보다는 더하기 수행
    num = int(data[i])
    if num  <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
