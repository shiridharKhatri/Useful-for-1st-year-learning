
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<Parent> parents = new ArrayList<>();

        Parent p1 = new Parent();
        p1.setName("Parent");
        parents.add(p1);

        Parent p2 = new Child();
        p2.setName("Son");
        parents.add(p2);
        ChildTwo p3 = new ChildTwo();
        p3.setHobbies("Hello World");
        parents.add(p3);
        parents.forEach((s)->{
            System.out.println(s.getName());
            if(s instanceof ChildTwo){
                ChildTwo ss = (ChildTwo)s;
                System.out.println(ss.getHobbies());
            }
            else if(s instanceof Child){
                Child ss = (Child)s;
                System.out.println(ss.getHobbies());
            }
        });
    }
}