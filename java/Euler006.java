public class Euler006{
    public static void main(String[] args){
        System.out.println(p006());
    }

    private static int p006(){
        int squareSum = 0;

        for(int i = 1; i <= 100; ++i){
            squareSum += i * i;
        }

        // sum of 1 .. n = n * (n + 1) / 2
        int sum  = 50 * 101;
        return sum * sum - squareSum;
    }
}
