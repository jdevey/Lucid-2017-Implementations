w = int(input())
for _ in range(w):
    p, m, n = list(map(int, input().split()))
    c = m + n
    if p % c < m:
        print('Jacob')
    else:
        print('Megan')