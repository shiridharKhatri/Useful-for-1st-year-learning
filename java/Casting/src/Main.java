public class Main {
    public static void fishDownCasting(Animal animal){
        if(animal instanceof Fish){
            Fish fis = (Fish)animal;
            fis.breathe();
        }
    }
    public static void main(String[] args) {
        Fish fish = new Fish();

        fish.locomotion();
        fish.breathe();

        System.out.println(fish.name +" "+ fish.size);
        Dog dog = new Dog();
        dog.locomotion();
        dog.breathe();
        System.out.println(dog.name + " "+dog.size);
        Animal animal = new Animal();
        animal.locomotion();

        System.out.println(animal.name);
        Animal fish1 =  new Fish();
        fish1.locomotion();
        fishDownCasting(fish);

        Fish fish2 = new Fish();
        fish2.locomotion();
        fish2.breathe();
    }
}
