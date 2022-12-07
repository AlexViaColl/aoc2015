def solve(s):
    n = 0
    for i, c in enumerate(s):
        if c == '(':
            n += 1
        elif c == ')':
            n -= 1
        else:
            raise

        if n == -1:
            return i + 1

    raise

with open('input.txt') as f:
    print(solve(f.read()))
