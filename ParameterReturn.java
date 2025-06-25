public class ParameterReturn {
    static int myMethod( int x, int y ){
        return x + y ;
    }
    public static void main(String[] args) {
        int z = myMethod(4, 17);
        System.out.println("Boy is Actual Age is : " + z);
    }
    
}
