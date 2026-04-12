
class Man {
    void role(){
        System.out.println("I'm an Employee in Office");
    }
    
}
class Student extends Man{

    @Override
    void role(){
        System.out.println("\n I'm the MCA Final year student of SRM Valliammai Engineering College \n");
    }
}

public class Main{
    public static void main(String[] args) {

        Man okay = new Student();

        okay.role();
        
    }
}
