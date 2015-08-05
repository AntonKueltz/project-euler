import java.math.BigInteger;
import java.util.ArrayList;

public class Euler003{
    public static void main(String[] args){
        System.out.println(p003());
    }

    private static int p003(){
        BigInteger n = new BigInteger("600851475143");
        ArrayList<Integer> primes = EulerUtil.genPrimesUpTo(1000000);

        for(Integer prime : primes){
            BigInteger bPrime = new BigInteger(String.valueOf(prime));

            if(n.mod(bPrime).signum() == 0){
                n = n.divide(bPrime);
                if(n.compareTo(bPrime) < 1) return prime;
            }
        }

        return -1;
    }
}
