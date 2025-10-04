
interface Animal{
    void sound();  // Abstract class
}
class Dog implements Animal{
    public void sound() {
        System.out.println("Voooooo");
    }
}
public class InterfaceExample {
    public static void main(String[] args) {
        Dog myDog = new Dog();
        myDog.sound();
    }
}
