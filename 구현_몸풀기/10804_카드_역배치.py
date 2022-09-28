cards = [i for i in range(1, 21)]

for _ in range(10):
    a, b = map(int, input().split())

    cards = cards[0:a-1] + list(reversed(cards[a-1:b])) + cards[b:]

for i in cards:
    print(i, end= ' ')