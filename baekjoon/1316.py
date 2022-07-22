# 그룹 단어 체커
# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램

N = int(input())
total = 0
for i in range(N):
    count = 0
    word = list(input())
    start = word[0]
    for j in range(1,len(word)):
        #print(word[j])
        #print(start)
        if word[j] == start:
            count += 1
        start = word[j]

    if (count != 0) or (len(word) == len(set(word))):
        #print(word)
        total += 1 
print(total)