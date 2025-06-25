public class Parameter {
    static void myMethod(String name, int age){
        System.out.print(name + " age is " + age);
        if ( age < 18 ) {
            System.out.println(" Access Denied! - Because Your Miner ");
        }else{
            System.out.println(" Access Granted! ");
        }
    }
    public static void main(String[] args) {
        myMethod( "Raja", 21);
        myMethod("Arun", 17);
        myMethod("Selva Raj", 28);
    }
    
}
