import java.util.ArrayList;
import java.util.Scanner;

public class OddEven {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        ArrayList<Integer> odd = new ArrayList<>();
        ArrayList<Integer> even = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            System.out.print("Enter number >> ");
            int inputNumber = input.nextInt();
            if(inputNumber % 2 == 0){
                even.add(inputNumber);
            }else{
                odd.add(inputNumber);
            }
        }
        System.out.println("Odd numbers are : " + odd);
        System.out.println("Even numbers are : " + even);
        odd.removeLast();
        even.removeFirst();
        System.out.println("Odd numbers after removing last index : " + odd);
        System.out.println("Even numbers after removing first index : " + even);

    }
}
