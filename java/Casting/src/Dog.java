public class Dog extends Animal{
    int noOfLegs = 4;

    @Override
    public void locomotion(){
        System.out.println("Move using legs");
    }
    public void breathe(){
        System.out.println("Breathe through lungs");
    }
}
