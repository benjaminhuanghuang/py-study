from collections import deque

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print q     # [1,2,3]
q.append(4)
print q     # [2,3,4]
q.append(5)
print q     # [3,4,5]

q.appendleft(4)

q.pop()

q.popleft()

 
