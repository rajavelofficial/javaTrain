class Over{
    
    static{
        
        System.out.println("Over class is loaded by the JVM!");
    }

    public void display(){
        
        System.out.println("Method of Over class is executed.");
    }
}

public class heap{
    public static void main(String[] args) throws Exception{
        
        System.out.println("Main method started.");

        // Loading the class explicitly using Class.forName()
        Class.forName("Over");

        System.out.println("Class loaded successfully. ( Happy Hacking )");

        // Creating object to execute method
        Over obj = new Over();
        obj.display();
    }
}
