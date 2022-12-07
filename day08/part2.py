def solve(s):
    n = 0
    for l in s.splitlines():
        in_memory = 0
        encoded = 6 
        in_escape = False
        for i in range(1, len(l) - 1):
            if l[i] != '\\' and not in_escape:
                in_memory += 1
                encoded += 1
            elif l[i] == '\\' and not in_escape:
                in_escape = True
                encoded += 2
            elif l[i] == '\\' and in_escape:
                in_memory += 1
                encoded += 2
                in_escape = False
            elif l[i] == '"' and in_escape:
                in_memory += 1
                encoded += 2
                in_escape = False
            elif l[i] == 'x' and in_escape:
                in_memory += 1
                encoded += 1
                hex_digits = 0
            elif in_escape and hex_digits < 2:
                hex_digits += 1
                encoded += 1
                if hex_digits == 2:
                    in_escape = False
            else:
                raise

        n += encoded - len(l)

    return n

def main():
    with open('input.txt') as f:
        print(solve(f.read()))

if __name__ == '__main__':
    main()
