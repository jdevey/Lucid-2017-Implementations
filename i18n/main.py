n = int(input())
for _ in range(n):
  s = input().strip()
  if len(s) > 2:
    print(s[0] + str(len(s) - 2) + s[-1])
  else:
    print(s)
