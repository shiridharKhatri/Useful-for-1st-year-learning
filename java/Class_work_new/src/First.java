public class First {
 public static void main(String[] args) {
    int a = 10;
    int b = 20;
     System.out.println("a+b = "+(a+b));


     String ujjal = "Khatra";

     int ristedar = 67;

     double x = 40;
     int y = (int)40.0;


First first = new First();
     first.givingGift(ujjal);
     first.givingGift(ristedar);
     first.givingGift(ujjal, ristedar);


     Second second = new Second();

     second.givingGift(ujjal);
     second.givingGift(ristedar);
     second.givingGift(ujjal, ristedar);

 }

 public  void givingGift(String keihaina){
     System.out.println("Khatra Gift");
 }


 public  void givingGift(int hajurHajur){
     System.out.println("Khattam Gift");
 }

 public  void givingGift(String cycle, int qty){
     System.out.println(qty+" ota "+cycle+" Paiyo");
 }

}
