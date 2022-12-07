def has_pair(s):
    pairs = set()
    for i in range(len(s) - 1):
        pair = s[i] + s[i + 1]
        if pair in s[i+2:]:
            return True
    return False

def has_in_between(s):
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            return True
    return False

def is_nice(s):
    return has_pair(s) and has_in_between(s)

def solve(s):
    n = 0
    lines = s.splitlines()
    for l in lines:
        if is_nice(l.strip()):
            n += 1
    return n

def main():
    with open('input.txt') as f:
        print(solve(f.read()))

if __name__ == '__main__':
    main()
