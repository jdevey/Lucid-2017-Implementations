c, n = list(map(int, input().split()))
pf = []
nf = []
for _ in range(n):
    fl = int(input())
    if fl > 0:
        pf.append(fl)
    elif fl < 0:
        nf.append(fl)

spf = sorted(pf, reverse=True)
snf = [abs(x) for x in sorted(nf)]
moves = 0

floors = [spf, snf]
if len(spf) == 0 and len(snf) == 0:
    pass
elif len(spf) == 0:
    moves -= snf[0]
elif len(snf) == 0:
    moves -= spf[0]
else:
    moves -= max(spf[0], snf[0])
    

for i, l in enumerate(floors):
    while len(l) > 0:
        moves += l[0] * 2
        if c < len(l):
            l = l[c:]
        else:
            l = []

seconds = moves * 20
minutes = 0
hours = 0
if seconds >= 60:
    minutes = seconds // 60
    seconds = seconds % 60
if minutes >= 60:
    hours = minutes // 60
    minutes = minutes % 60

if hours % 24 < 3 or hours % 24 > 14:
    tod = 'AM'
else:
    tod = 'PM'

hour = (9 + hours) % 12
if hour == 0:
    hour = 12
if hour < 10:
    hour = '0' + str(hour)
if minutes < 10:
    minutes = '0' + str(minutes)
if seconds < 10:
    seconds = '0' + str(seconds)

time = str(hour) + ':' + str(minutes) + ':' + str(seconds) + ' ' + tod
print(time)
