def solve(s):
    s = s.strip()
    for i in range(40):
        new_s = ''
        n = 0
        last = None
        for c in s:
            if last is None:
                last = c
                n = 1
            elif c == last:
                n += 1
            else:
                new_s += f'{n}{last}'
                n = 1
                last = c
        if n != 0:
            new_s += f'{n}{last}'

        s = new_s
        
    return len(s)

def main():
    with open('input.txt') as f:
        print(solve(f.read()))

if __name__ == '__main__':
    main()

# 294954 too high
