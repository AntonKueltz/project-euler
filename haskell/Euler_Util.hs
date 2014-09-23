module Euler_Util where

primes = 2 : 3 : sieve (tail primes) [5,7..] where
	sieve (p:ps) xs = h ++ sieve ps [x | x <- t, mod x p /= 0] where
		(h,~(_:t)) = span (< p*p) xs