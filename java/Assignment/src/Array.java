import java.util.ArrayList;

public class Array {
    public static void main(String[] args) {
        ArrayList<Integer> nameStr = new ArrayList<>();
        nameStr.add(1);
        nameStr.add(2);
        nameStr.add(3);
        nameStr.add(4);
        nameStr.add(5);
        nameStr.remove((int)2);
        System.out.println(nameStr);
    }
}
