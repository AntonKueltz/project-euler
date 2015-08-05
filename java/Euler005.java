public class Euler005{
    public static void main(String[] args){
        System.out.println(p005());
    }

    private static int p005(){
        int minProd = 1;

        for(int i = 1; i <= 20; ++i){
            minProd *= (i / EulerUtil.gcd(i, minProd));
        }

        return minProd;
    }
}
