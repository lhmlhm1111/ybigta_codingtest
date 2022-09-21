n = int(input())
exp = input()
num_dict = {chr(alpha):int(input()) for alpha, _ in enumerate(range(n), start=65)}

stack = []
for e in exp:
    if e.isalpha():
        stack.append(num_dict[e])
    elif e == '+':
        a = stack.pop()
        b = stack.pop()
        
        num = a + b
        stack.append(num)
    elif e == '*':
        a = stack.pop()
        b = stack.pop()
        
        num = a * b
        stack.append(num)

    elif e == '/':
        a = stack.pop()
        b = stack.pop()
        
        num = b / a
        stack.append(num)

    elif e == '-':
        a = stack.pop()
        b = stack.pop()
        
        num = b - a
        stack.append(num)

print(f'{stack[0]:.2f}')

