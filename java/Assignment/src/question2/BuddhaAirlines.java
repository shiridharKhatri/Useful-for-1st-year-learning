package question2;
import java.util.ArrayList;
public class BuddhaAirlines implements Airlines{
    int totalSeats = 30;
    ArrayList<String> bookedSeat = new ArrayList<>();

    @Override
    public int getTotalAvailableSeats() {
        return totalSeats - bookedSeat.toArray().length;
    }

    @Override
    public void printName() {
        System.out.println("Buddha Airlines");
    }

    @Override
    public boolean book(String name, String passportNo) {
        if(getTotalAvailableSeats() <= totalSeats){
            if(bookedSeat.contains(passportNo)){
                System.out.println("You have already booked the flight with passport number : "+passportNo);
            }else{
                bookedSeat.add(passportNo);
                System.out.println("Booked Seat for " + name + " of " + getTotalAvailableSeats());
            }
            return true;
        }else{
            System.out.println("Booking not available th seats are full!");
            return false;
        }
    }
}
