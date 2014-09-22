def euler197():
    f = lambda x: int(2**(30.403243784-x*x)) * 10**-9
    result = f(-1)
    prev = 0, result

    # assume the series converges, at which point answer won't change
    while prev != (f(result), result):
        prev = result, f(result)
        result = f(result)

    return result + f(result)

if __name__ == "__main__":
    print euler197()
