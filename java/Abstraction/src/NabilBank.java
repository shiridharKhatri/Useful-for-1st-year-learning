public class NabilBank implements Bank{
    @Override
    public void withdraw() {
      System.out.println("Nabil Bank withdrawal");
    }

    @Override
    public void deposit() {
        System.out.println("Nabil Bank deposit");
    }

    @Override
    public void sms() {
        System.out.println("Nabil Bank sms");
    }

    @Override
    public void mobileBanking() {
        System.out.println("Nabil Bank mobile");
    }

    @Override
    public void atm() {
        System.out.println("Nabil Bank atm");
    }

    public static void main(String[] args) {
        Bank bank = new NabilBank();
        bank.withdraw();
        bank.deposit();
        bank.sms();
        bank.mobileBanking();
        bank.atm();
    }
}
