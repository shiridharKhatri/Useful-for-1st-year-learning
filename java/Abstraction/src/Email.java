import java.util.Scanner;
public class Email implements Message{
    Scanner sc = new Scanner(System.in);
    @Override
    public String getMessage() {
        return sc.nextLine();
    }

    @Override
    public String getRecipient() {
        return sc.nextLine();
    }

    @Override
    public void print() {
        Email email = new Email();
        email.getRecipient();
        email.getMessage();
    }
}
