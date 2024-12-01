import java.util.ArrayList;

public class ArraylistIntoArray {
    public static void main(String[] args) {
        int[] arr = new int[5];
        ArrayList<Integer> number = new ArrayList<>();
        number.add(421);
        number.add(26);
        number.add(863);
        number.add(457);
        number.add(975);

        for(int i =0; i<number.size(); i++){
            arr[i] = number.get(i);
        }

       for(int element:arr){
           System.out.println(element);
       }
    }
}
