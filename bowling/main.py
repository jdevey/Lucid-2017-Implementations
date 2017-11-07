n = int(input())
for _ in range(n):
    l = list(map(int, input().split()))
    runningTotal = 0
    current = 0
    frame = 1
    while current < len(l) and frame <= 10:
        if l[current] == 10:
            runningTotal += 10 + l[current + 1] + l[current + 2]
            current += 1
            frame += 1
        elif l[current] + l[current + 1] == 10:
            runningTotal += 10 + l[current + 2]
            current += 2
            frame += 1
        else:
            runningTotal += l[current] + l[current + 1]
            current += 2
            frame += 1
    print(runningTotal)