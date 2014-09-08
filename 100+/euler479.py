import numpy

def euler479():
    # 1/x = (k/x)^2 * (k+x^2) - kx
    # 1/x = k^2/x^2 * (k+x^2) - kx
    # 1/x = (k^3 + k^2x^2) / x^2 -kx
    # 1/x = k^3/x^2 + k^2 - kx
    # 1 = k^3 / x + k^2x - kx^2
    # 0 = k^3 / x + k^2x - kx^2 - 1
    # 0 = k^3 - x + k^2x^2 - kx^3
    pass

if __name__ == "__main__":
    print euler479()
