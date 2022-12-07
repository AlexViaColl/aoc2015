def solve(s):
    lines = s.splitlines()
    lights = []
    for i in range(1000):
        lights.append([0] * 1000)
    for i, line in enumerate(lines):
        if line.startswith("turn"):
            _, _, start, _, end = line.split()
        elif line.startswith("toggle"):
            _, start, _, end = line.split()
        start = tuple(map(int, start.split(',')))
        end = tuple(map(int, end.split(',')))

        for x in range(start[0], end[0]+1):
            for y in range(start[1], end[1]+1):
                if line.startswith("turn on"):
                    lights[x][y] += 1
                elif line.startswith("turn off"):
                    if lights[x][y] > 0:
                        lights[x][y] = lights[x][y] - 1
                    else:
                        lights[x][y] = 0
                elif line.startswith("toggle"):
                    lights[x][y] += 2

    n = 0
    for l in lights:
        for z in l:
            n += z
    return n

with open('input.txt') as f:
    print(solve(f.read()))
