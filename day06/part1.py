def solve(s):
    lines = s.splitlines()
    on = set()
    for line in lines:
        if line.startswith("turn"):
            _, _, start, _, end = line.split()
        elif line.startswith("toggle"):
            _, start, _, end = line.split()
        start = tuple(map(int, start.split(',')))
        end = tuple(map(int, end.split(',')))

        for x in range(start[0], end[0]+1):
            for y in range(start[1], end[1]+1):
                if line.startswith("turn on"):
                    on.add((x, y))
                elif line.startswith("turn off") and (x, y) in on:
                    on.remove((x, y))
                elif line.startswith("toggle"):
                    if (x, y) in on:
                        on.remove((x, y))
                    else:
                        on.add((x, y))
    return len(on)

with open('input.txt') as f:
    print(solve(f.read()))
