def solve(s):
    n = 0
    for c in s:
        if c == '(':
            n += 1
        elif c == ')':
            n -= 1
        else:
            raise
    return n

def main():
    with open('input.txt') as f:
        print(solve(f.read()))

if __name__ == '__main__':
    main()
