def next_password(password):
    if password[-1] != 'z':
        return password[:-1] + chr(ord(password[-1]) + 1)
    else:
        return next_password(password[:-1]) + 'a'

def is_valid(pw):
    has_stair = False
    for i in range(2, len(pw)):
        if ord(pw[i - 2]) + 1 == ord(pw[i - 1]) and ord(pw[i - 1]) + 1 == ord(pw[i]):
            has_stair = True
    if not has_stair:
        return False

    if 'i' in pw or 'o' in pw or 'l' in pw:
        return False
    
    last_pair_start = -1
    pairs = 0
    for i in range(len(pw) - 1):
        if pw[i] == pw[i + 1]:
            if last_pair_start == -1:
                pairs += 1
                last_pair_start = i
            elif i > last_pair_start + 1:
                pairs += 1
                last_pair_start = i
    if pairs < 2:
        return False

    return True

def solve(s):
    s = s.strip()
    while not is_valid(s):
        s = next_password(s)

    s = next_password(s)
    while not is_valid(s):
        s = next_password(s)

    return s

def main():
    with open('input.txt') as f:
        print(solve(f.read()))

if __name__ == '__main__':
    main()
