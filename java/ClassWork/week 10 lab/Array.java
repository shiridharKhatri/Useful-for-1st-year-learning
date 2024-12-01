
import java.util.Scanner;
public class Array
{ 
    public static void main(String[] args){
        int[] number = new int[10];

        Scanner input = new Scanner(System.in);
        System.out.println("Enter any number : ");
        for(int i=0; i < number.length; i++){
            number[i] = input.nextInt();
        }
        
        int[] reverse = new int[10];
        for(int j =0; j<reverse.length; j++){
            reverse[j] = number[reverse.length - 1 - j];
            System.out.print(" "+ reverse[j]);
        }
    }
}
