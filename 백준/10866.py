import sys
from collections import deque

queue = deque()

def push_front(x):
    queue.appendleft(x)

def push_back(x):
    queue.append(x)

def pop_front():
    if not queue:
        print(-1)
    else:
        print(queue.popleft())

def pop_back():
    if not queue:
        print(-1)
    else:
        print(queue.pop())

def size():
    print(len(queue))

def empty():
    if queue:
        print(0)
    else:
        print(1)

def front():
    if queue:
        print(queue[0])
    else:
        print(-1)

def back():
    if queue:
        print(queue[-1])
    else:
        print(-1)

n = int(sys.stdin.readline())

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push_front':
        push_front(command[1])
    elif command[0] == 'push_back':
        push_back(command[1])
    elif command[0] == 'pop_front':
        pop_front()
    elif command[0] == 'pop_back':
        pop_back()
    elif command[0] == 'size':
        size()  
    elif command[0] == 'empty':
        empty()  
    elif command[0] == 'front':
        front()
    elif command[0] == 'back':
        back()
    else:
        break