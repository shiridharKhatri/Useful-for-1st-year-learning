public class Parent {
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    private int id;
    private String name;
    private String address;

    public void talk(){
        System.out.println("Talking");
    }

    public void walk(){
        System.out.println("Walking");
    }
}