euler001 = sum [n | n <- [1..999], mod n 3 == 0 || mod n 5 == 0]

main = print euler001