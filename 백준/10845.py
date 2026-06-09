import sys
from collections import deque

queue = deque()

def push(x):
    queue.append(x)

def pop():
    if not queue:
        print(-1)
    else:
        print(queue.popleft())

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

    if command[0] == 'push':
        push(command[1])
    elif command[0] == 'pop':
        pop()
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