
public class Avgvalue
{
    public static void main(String[] args){
        int[] numbers = {10, 20, 30, 40 , 50};
        int sumNum = 0;
        for(int i = 0; i<numbers.length; i++){
            sumNum+=numbers[i];
        }
        System.out.println("Average value is : " + sumNum/numbers.length);

    }
}
