from fractions import gcd

def euler05():
        """
        2520 is the smallest number that can be divided by each of the numbers
        from 1 to 10 without any remainder.

        What is the smallest positive number that is evenly divisible by all of
        the numbers from 1 to 20?
        """
        num = 1
        
        for mult in range(1, 21):
                num *= mult / gcd(num, mult)

        return num
        
if __name__ == "__main__":
        print euler05()
