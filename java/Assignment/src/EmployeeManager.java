import java.util.Scanner;
public class EmployeeManager extends Employee{
    @Override
    public void add(String name) {
        if(!employees.contains(name)){
            employees.add(name);
            System.out.println(name+" has been added");
       }else{
            System.out.println(name+" has already been added");
        }
    }

    @Override
    public void remove(String name) {
        if(!employees.contains(name)){
            System.out.println(name+" Is not in the list");
        }else{
            employees.remove(name);
            System.out.print(name + " Has been removed ");
            System.out.println(employees.toArray().length + " peoples are available they are "+ employees);
        }
    }
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        EmployeeManager manager = new EmployeeManager();
        boolean isAdded = false;
        int addedCount = 0;
        while(!isAdded){
            System.out.print("Enter employee name >> ");
            String name = input.nextLine();
            if(manager.employees.contains(name)){
                manager.add(name);
            }else{
                manager.add(name);
                addedCount++;
                if(addedCount == 5){
                    isAdded = true;
                }
            }
        }

        System.out.print("Enter employee name to search >> ");
        manager.search(input.nextLine());

        boolean isRemoved = false;
        int removedCount = 0;
        while (!isRemoved){
            System.out.print("Enter employee name to remove >> ");
            String name = input.nextLine();
            if(manager.employees.contains(name)){
                manager.remove(name);
                removedCount++;
                if(removedCount == 2){
                    isRemoved = true;
                }
            }else{
                manager.remove(name);
            }
        }
    }
}
