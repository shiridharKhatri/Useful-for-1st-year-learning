public class MessagingService {
    public void methodsDiaplay(Message message){
        if(message instanceof Sms){
            Sms sms = (Sms)message;
            sms.print();
        }
        if(message instanceof Email){
            Email email = (Email)message;
            email.print();
        }
    }
    public static void main(String[] args) {
        MessagingService service = new MessagingService();
        Sms obj = new Sms();
        service.methodsDiaplay(obj);
        Email objEm = new Email();
        service.methodsDiaplay(objEm);
    }
}
