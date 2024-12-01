public class Game{
    private String name;
    private double version;
    public Game(String name, double version){
        this.name = name;
        this.version = version;
    }

    public String getName(){
        return name;
    }

    public double getVersion(){
        return version;
    }

    public void setName(String name){
        this.name = name;
    }

    public void setVersion(double name){
        this.version = version;
    }

    public void print(){
        System.out.println(name);
        System.out.println(version);
    }

    public static void main(){
        Game obj = new Game("CallOfDuty", 23.5);
        System.out.println(obj.getName());
        System.out.println(obj.getVersion());

    }
}