import java.util.ArrayList;
abstract class Employee {
    ArrayList<String> employees = new ArrayList<>();
    public void search(String name){
            if (employees.contains(name)) {
                System.out.println("Employee found of name : " + name);
            }else {
                System.out.println("Employee not found of name : " + name);
            }
    }
    public abstract void add(String name);
    public abstract void remove(String name);
}
