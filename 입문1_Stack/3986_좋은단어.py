n = int(input())
cnt = 0
for _ in range(n):
    inp = input()
    stack = []
    for i in inp:
        if not stack:
            stack.append(i)
        else:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
    
    if not stack:
        cnt += 1

print(cnt)
