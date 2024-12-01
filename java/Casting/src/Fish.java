public class Fish extends Animal{
    float size = 23;

    @Override
    public void locomotion(){
        System.out.println("Swimming using fins");
    }

    public void breathe(){
        System.out.println("Breathe through gills");
    }
}
