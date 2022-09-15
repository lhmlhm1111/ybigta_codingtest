import sys
input = sys.stdin.readline

n = int(input())

stack = []

for _ in range(n):
    inp = input().split()
    if inp[0] == 'push':
        stack.append(int(inp[1]))
    
    elif inp[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    
    elif inp[0] == 'size':
        print(len(stack))

    elif inp[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif inp[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
