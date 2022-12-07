def solve(s):
    presents = set()
    pos = [[0, 0], [0, 0]]
    for i, c in enumerate(s):
        if c == '<':
            pos[i % 2][0] -= 1
        elif c == '>':
            pos[i % 2][0] += 1
        elif c == '^':
            pos[i % 2][1] += 1
        elif c == 'v':
            pos[i % 2][1] -= 1
        else:
            raise
        presents.add(tuple(pos[0]))
        presents.add(tuple(pos[1]))
    return len(presents)

with open('input.txt') as f:
    print(solve(f.read()))
