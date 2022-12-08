import json

c = 0

def count(n):
    global c
    if isinstance(n, dict):
        if not 'red' in n.values():
            for k in n:
                count(n[k])
    elif isinstance(n, list):
        for x in n:
            count(x)
    elif isinstance(n, int):
        c += n

def solve(s):
    root = json.loads(s)
    count(root)

    return c

def main():
    with open('input.txt') as f:
        print(solve(f.read()))

if __name__ == '__main__':
    main()
