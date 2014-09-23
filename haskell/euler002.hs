fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

euler002 = sum [n | n <- takeWhile (<4000000) fibs, mod n 2 == 0]

main = print euler002