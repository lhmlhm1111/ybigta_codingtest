t = int(input())

for _ in range(t):
    stack = []
    inp = input()
    for i in inp:
        if not stack:
            stack.append(i)
        else:
            if i == '(':
                stack.append(i)
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(i)
    
    if stack:
        print('NO')
    else:
        print('YES')

