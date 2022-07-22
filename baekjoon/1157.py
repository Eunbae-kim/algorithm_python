# 단어 공부
# 알파벳 대소문자로 된 단어가 주어지면, 
# 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
# 단, 대문자와 소문자를 구분하지 않는다.

# 입력 : 
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력 :
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

input_str = str(input())
input_str = input_str.upper()
#print(input_str)
compare = list(set(input_str)) #문자열에 나온 값들을 중복 제거 해서 추가
#print(compare)
count_list =[0]*len(compare)

for i in range(len(input_str)):
    for j in range(len(compare)):
        if input_str[i] == compare[j]:
            count_list[j] += 1

if count_list.count((max(count_list))) > 1:
    print("?")
else:
    print(compare[count_list.index((max(count_list)))])
