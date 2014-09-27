import numpy

def get_BOP(seq):
    degree = len(seq)
    weights = numpy.polyfit(range(1, degree+1), seq, degree-1)

    BOP = 0
    for e, weight in enumerate(weights[::-1]):
        BOP += weight*(degree+1)**e
    
    return BOP

def euler101():
    eq = lambda n: 1-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10
    seq = map(eq, range(1, 11))

    BOPsum = 0
    for k in range(1, len(seq)+1):
        BOPsum += get_BOP(seq[:k])
        
    return BOPsum

if __name__ == "__main__":
    print euler101()
