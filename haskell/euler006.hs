square n = n*n

euler006 = (square $ sum [1..100]) - (sum $ map square [1..100])

main = print euler006