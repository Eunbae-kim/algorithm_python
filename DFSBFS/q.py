from collections import deque

#큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력

# 오른쪽에서 들어와서 왼쪽으로 나가니까 순서를 바꿔주기
queue.reverse() #역순으로 바꾸기
print(queue)

