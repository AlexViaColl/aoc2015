def vowels(s):
    v = "aeiou"
    n = 0
    for c in s:
        if c in v:
            n += 1
    return n

def twice(s):
    prev = None
    for c in s:
        if prev is None:
            prev = c
            continue
        elif c == prev:
            return True
        prev = c
    return False

def not_in(s, l):
    for seq in l:
        if seq in s:
            return False
    return True

def is_nice(s):
    return vowels(s) >= 3 and twice(s) and not_in(s, ["ab", "cd", "pq", "xz"])

def solve(s):
    n = 0
    lines = s.splitlines()
    for l in lines:
        if is_nice(l.strip()):
            n += 1
    return n

with open('input.txt') as f:
    print(solve(f.read()))
