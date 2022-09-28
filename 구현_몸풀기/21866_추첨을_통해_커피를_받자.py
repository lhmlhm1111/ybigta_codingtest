scores = list(map(int, input().split()))
max_scores = [100,100,200,200,300,300,400,400,500]

total_score = 0
status = 'none'
for score, max_score in zip(scores, max_scores):
    if score > max_score:
        status = 'hacker'
        break
    total_score += score

if status != 'hacker' and total_score >= 100:
    status = 'draw'

print(status)