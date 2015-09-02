public class Euler004{
    public static void main(String[] args){
        System.out.println(p004());
    }

    private static int p004(){
        int max = 0;

        for(int i = 100; i < 1000; ++i){
            for(int j = i+1; j < 1000; ++j){
                int product = i * j;

                if(EulerUtil.isPalindrome(product) && product > max){
                    max = product;
                }
            }
        }

        return max;
    }
}
