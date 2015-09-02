def read_codes():
    f = open("p079_keylog.txt")
    return map(int, f.read().split("\n")[:-1])

def euler79():
    depend = []
    digits = []
    for _ in range(10): depend.append([])

    for code in read_codes():
        d = (code / 100, (code / 10) % 10, code % 10)
        for d_ in d: digits.append(d_)
        depend[d[2]] += [d[0], d[1]]
        depend[d[1]].append(d[0])

    digits = set(digits)
    depend = map(set, depend)
    passcode = []

    while set(passcode) != digits:
        for dig in digits:
            if depend[dig] == set(passcode): passcode.append(dig)

    return "".join(map(str, passcode))

if __name__ == "__main__":
    print euler79()
