import java.util.ArrayList;

public class ArrayToArrayList {
    public static void main(String[] args) {
        String[] namesStr = new String[5];
        ArrayList<String> namesList = new ArrayList<String>();
        namesStr[0] = "John";
        namesStr[1] = "Jane";
        namesStr[2] = "Doe";
        namesStr[3] = "Jack";
        namesStr[4] = "Jane";
        System.out.println("Before adding to array list : "+ namesList);
        for(String names : namesStr) {
           namesList.add(names);
        }
        System.out.println("After adding to array list : "+ namesList);
    }
}
