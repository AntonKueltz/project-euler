import java.util.ArrayList;

public class Euler007{
    public static void main(String[] args){
        System.out.println(p007());
    }

    private static int p007(){
        ArrayList<Integer> primes = EulerUtil.genPrimesUpTo(1000000);
        return primes.get(10000);
    }
}
