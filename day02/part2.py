def solve(s):
    lines = s.splitlines()
    n = 0
    for line in lines:
        l, w, h = map(int, line.split('x'))
        n += l*w*h
        if l >= w and l >= h:
            n += w*2 + h*2
        elif w >= l and w >= h:
            n += l*2 + h*2
        else:
            n += w*2 + l*2
    return n

with open('input.txt') as f:
    print(solve(f.read()))
