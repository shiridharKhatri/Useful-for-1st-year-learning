package question2;

public class AirlinesRunner {
    public static void main(String[] args) {
        Airlines nepalAirlines = new NepalAirlines();
        nepalAirlines.printName();
        nepalAirlines.book("Shiridhar", "DASER234");
        nepalAirlines.book("kaneki", "HDAKS878");
        nepalAirlines.book("dasdads", "HDAKS878");
        System.out.println("Available Seats " + nepalAirlines.getTotalAvailableSeats());

        Airlines buddhaAirlines = new BuddhaAirlines();
        buddhaAirlines.printName();
        buddhaAirlines.book("Touka", "KSUER234");
        buddhaAirlines.book("Tanjiro", "FGAKS878");
        buddhaAirlines.book("Ram", "RAM66578");
        System.out.println("Available Seats " + buddhaAirlines.getTotalAvailableSeats());
    }
}
