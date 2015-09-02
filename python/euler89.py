def build_minimal(num):
    if "VIIII" in num: num = num.replace("VIIII", "IX")
    if "IIII" in num: num = num.replace("IIII", "IV")
    if "VV" in num: num = num.replace("VV", "X")
    if "LXXXX" in num: num = num.replace("LXXXX", "XC")
    if "XXXX" in num: num = num.replace("XXXX", "XL")
    if "LL" in num: num = num.replace("LL", "C")
    if "DCCCC" in num: num = num.replace("DCCCC", "CM")
    if "CCCC" in num: num = num.replace("CCCC", "CD")
    return num

def euler89():
    f = open("p089_roman.txt", "r")
    numbers = f.read().split("\n")

    digits_saved = 0
    
    for num in numbers:
        minimal = build_minimal(num)
        digits_saved += len(num) - len(minimal)
    
    return digits_saved

if __name__ == "__main__":
    print euler89()
