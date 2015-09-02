public class Euler002{
    public static void main(String[] args){
        System.out.println(p002());
    }

    private static int p002(){
        int f1 = 1, f2 = 2, sum = 0;

        while(f2 <= 4000000){
            if((f2 & 1) != 1) sum += f2;

            int tmp = f2;
            f2 = f1 + tmp;
            f1 = tmp;
        }

        return sum;
    }
}
