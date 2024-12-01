import java.util.Scanner;

public class Compare {
    public static void main(String[] args) {
        int[] defaultNum = {2, 5, 4};
        int[] userInput = new int[defaultNum.length];
        Scanner input = new Scanner(System.in);

        for (int i = 0; i < defaultNum.length; i++) {
            System.out.print("Enter number: ");
            int number = input.nextInt();
            userInput[i] = number;
        }

        System.out.print("Common numbers are: ");
        for (int i = 0; i < defaultNum.length; i++) {
            for (int j = 0; j < userInput.length; j++) {
                if (defaultNum[i] == userInput[j]) {
                    System.out.print(defaultNum[i] + " ");
                }
            }
        }
    }
}
