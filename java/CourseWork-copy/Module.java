import java.util.Scanner;
public class Module{
    public static void main(String[] args){
        String[] module = new String[3];
        Scanner moduleInp = new Scanner(System.in);

        for(int i = 0; i<module.length; i++){
            System.out.print("Enter module");
            String userInpModule = moduleInp.nextLine();
            module[i] = userInpModule.toUpperCase();
        }
    
        System.out.println("Do you want to get recommendations?");
        String userInpModule = moduleInp.nextLine().toUpperCase();
        if(userInpModule.equals("YES")){
            for(int i = 0; i<module.length; i++){
                if(module[i].equals("IS")){
                    System.out.println("IS: I think you would like to learn web development.");
                }else if(module[i].equals("FOC")){
                    System.out.println("FOC: I think you have a great future in Machine learning");
                }else if(module[i].equals("PROGRAMMING")){
                    System.out.println("Programming: I think you have a great future in Programming");
                }else{
                    System.out.println(module[i] + ": As you wish");
                }
            }
        }else{
            System.out.println("Good luck!");
        }

    }
}