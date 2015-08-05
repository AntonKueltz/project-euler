public class Euler001{
    public static void main(String[] args){
        System.out.println(p001());
    }

    private static int p001(){
        int sum = 0;

        for(int i = 0; i < 1000; ++i){
            if(i % 3 == 0 || i % 5 == 0) sum += i;
        }

        return sum;
    }
}
