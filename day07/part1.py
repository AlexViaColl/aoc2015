signals = {}

def resolve(x):
    if isinstance(x, int) or x.isdecimal():
        return int(x)
    elif x in signals and isinstance(signals[x], int):
        return signals[x]
    else:
        return x

def solve(s):
    lines = s.splitlines()
    lines.sort(key=lambda line: line.split(' -> ')[1])      # sort alphabetically by destination
    lines.sort(key=lambda line: len(line.split(' -> ')[1])) # sort by destination length
    for l in lines:
        left, dest = l.split(' -> ')
        if 'AND' in left:
            left, _, right = left.split()
            left = resolve(left)
            right = resolve(right)
            if isinstance(left, int) and isinstance(right, int):
                signals[dest] = (left & right) & 0xffff
        elif 'OR' in left:
            left, _, right = left.split()
            left = resolve(left)
            right = resolve(right)
            if isinstance(left, int) and isinstance(right, int):
                signals[dest] = (left | right) & 0xffff
        elif 'LSHIFT' in left:
            left, _, right = left.split()
            left = resolve(left)
            right = resolve(right)
            if isinstance(left, int) and isinstance(right, int):
                signals[dest] = (left << right) & 0xffff
        elif 'RSHIFT' in left:
            left, _, right = left.split()
            left = resolve(left)
            right = resolve(right)
            if isinstance(left, int) and isinstance(right, int):
                signals[dest] = (left >> right) & 0xffff
        elif 'NOT' in left:
            _, left = left.split()
            left = resolve(left)
            if isinstance(left, int):
                signals[dest] = ~left & 0xffff
        else:
            signals[dest] = resolve(left)

    return resolve(signals['a'])

with open('input.txt') as f:
    print(solve(f.read()))
