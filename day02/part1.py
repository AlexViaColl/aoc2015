def solve(s):
    lines = s.splitlines()
    n = 0
    for line in lines:
        l, w, h = map(int, line.split('x'))
        n += 2*l*w + 2*w*h + 2*h*l
        if l >= w and l >= h:
            n += w*h
        elif w >= l and w >= h:
            n += l*h
        else:
            n += w*l
    return n

with open('input.txt') as f:
    print(solve(f.read()))
