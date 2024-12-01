import java.util.Scanner;
public class Array{
    public static void main(){
        int[] sum =new int[6];
        int total = 0;
        for(int i = 0; i<sum.length; i++){
            Scanner input = new Scanner(System.in);
            System.out.print("");
            sum[i] = input.nextInt();
            total+=sum[i];
        }
        System.out.println(total);
    }
}