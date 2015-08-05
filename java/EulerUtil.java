import java.util.ArrayList;
import java.util.BitSet;

public class EulerUtil{
    public static ArrayList<Integer> genPrimesUpTo(int n){
        ArrayList<Integer> primes =  new ArrayList<Integer>();
        BitSet isPrime = new BitSet(n);
        isPrime.set(0, n);

        for(int i = 2; i < n; ++i){
            if(isPrime.get(i)){
                primes.add(i);

                for(int fac = i * 2; fac < n; fac += i){
                    isPrime.clear(fac);
                }
            }
        }

        return primes;
    }

    public static boolean isPalindrome(int n){
        String s = String.valueOf(n);
        int len = s.length();

        for(int i = 0; i < len / 2; ++i){
            if(s.charAt(i) != s.charAt((len - 1) - i)) return false;
        }

        return true;
    }

    public static int gcd(int a, int b){
        while(b != 0){
            int r = a % b;
            a = b;
            b = r;
        }

        return a;
    }
}
