import java.util.Scanner;
public class Sms implements Message{
Scanner sc = new Scanner(System.in);
    @Override
    public String getMessage() {
        System.out.println("Enter message here >> ");
        return sc.nextLine();
    }

    @Override
    public String getRecipient() {
        System.out.println("Enter number here >> ");
        int number = sc.nextInt();

        if(number < 10){
            return "Invalid mobile number";
        }else{
            return "Valid mobile number";
        }
    }
    @Override
    public void print() {
        Sms sms = new Sms();
        sms.getMessage();
        sms.getRecipient();
    }
}
