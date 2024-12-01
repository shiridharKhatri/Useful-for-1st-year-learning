public interface Message {
    public String getMessage();
    public void print();
    public String getRecipient();
    default void printConnection(){
        System.out.println(" print connection is successful");
    }
}
