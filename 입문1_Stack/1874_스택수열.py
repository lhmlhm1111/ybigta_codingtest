n = int(input())
stack = []
answer = []
cnt = 1
cond = True

for i in range(n):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        answer.append('+')
        cnt += 1
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        cond = False

if cond == False:
    print('NO')
else:
    for i in answer:
        print(i)

