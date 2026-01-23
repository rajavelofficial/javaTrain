class Varity{
    public void displayApple(){
        System.out.println("This is Apple, Color is Red.");
    }
    public void displayOrange(){
        System.out.println("This is Orange, Color is Orange.");
    }
}

public class Fruits {
    public static void main(String[] args) {
        Varity one = new Varity();
        one.displayApple();

        System.out.println(Varity.class.getClassLoader());
    }
    
}
/*
// this Output creating object for class and call the method
This is Apple, Color is Red.

//this one load the class loader( the Vatity class in VS code is Memory class loader)
com.sun.tools.javac.launcher.MemoryClassLoader@17776a8
*/