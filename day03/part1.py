def solve(s):
    presents = set()
    x, y = 0, 0
    for c in s:
        if c == '<':
            x -= 1
        elif c == '>':
            x += 1
        elif c == '^':
            y += 1
        elif c == 'v':
            y -= 1
        else:
            raise
        presents.add((x, y))
    return len(presents)

with open('input.txt') as f:
    print(solve(f.read()))
