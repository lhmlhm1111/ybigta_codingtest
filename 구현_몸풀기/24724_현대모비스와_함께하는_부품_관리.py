import sys
input = sys.stdin.readline

t = int(input())

for i in range(1, t+1):
    n = int(input())
    a, b = map(int, input().split())
    print(f"Material Management {i}")
    for _ in range(n):
        u, v = map(int, input().split())
    print("Classification --- End!")