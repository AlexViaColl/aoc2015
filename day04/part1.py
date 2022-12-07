import hashlib

def solve(s):
    i = 1
    while True:
        m = hashlib.md5()
        txt = s.strip() + str(i)
        m.update(txt.encode())
        if m.hexdigest().startswith('0'*5):
            return i
        i += 1

with open('input.txt') as f:
    print(solve(f.read()))
