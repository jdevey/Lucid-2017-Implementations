# This one is really ugly because we were just trying to sqeeze it in at the end
# and never quite got it to work.
n = int(input())
for _ in range(n):
    x, y, w, h = list(map(int, input().split()))
    c = input().strip()
    ex, ey = list(map(int, input().split()))
    whprop = w / h
    trx = x + w
    tly = y
    tlx = x
    tryy = y
    bly = y + h
    blx = x
    bry = y + h
    brx = x + w
    if c == 'BottomRight':
        fx = tlx
        fy = tly
        if abs(ex - tlx) / abs(ey - tly):
            la = 'X'
        else:
            la = 'Y'
        if la == 'X':
            fh = abs(ex - tlx)
            fw = fh / whprop
        else:
            fh = abs(ey - tly)
            fw = fh * whprop
        if ex < tlx:
            fx = abs(tlx - fh)
        if ey < tly:
            fy = abs(tly - fw)
        print(int(fx), int(fy), int(fh), int(fw))

    elif c == 'TopLeft':
        fx = brx
        fy = bry
        if abs(ex - brx) / abs(ey - bry):
            la = 'X'
        else:
            la = 'Y'
        if la == 'X':
            fh = abs(ex - brx)
            fw = fh / whprop
        else:
            fh = abs(ey - bry)
            fw = fh * whprop
        if ex > brx:
            fx = abs(brx - fh)
        if ey > bry:
            fy = abs(bry - fw)
        print(int(fx), int(fy), int(fh), int(fw))

    elif c == 'TopRight':
        fx = blx
        fy = bly
        if abs(ex - blx) / abs(ey - bly):
            la = 'X'
        else:
            la = 'Y'
        if la == 'X':
            fh = abs(ex - blx)
            fw = fh / whprop
        else:
            fh = abs(ey - bly)
            fw = fh * whprop
        if ex < blx:
            fx = abs(blx - fh)
        if ey > bly:
            fy = abs(bly - fw)
        print(int(fx), int(fy), int(fh), int(fw))
    elif c == 'BottomLeft':
        fx = trx
        fy = tryy
        if abs(ex - trx) / abs(ey - tryy):
            la = 'X'
        else:
            la = 'Y'
        if la == 'X':
            fh = abs(ex - trx)
            fw = fh / whprop
        else:
            fh = abs(ey - tryy)
            fw = fh * whprop
        if ex > trx:
            fx = abs(trx - fh)
        if ey < tryy:
            fy = abs(tryy - fw)
        print(int(fx), int(fy), int(fh), int(fw))