public class ParameterOverload {
    static int plusMethod(int x, int y){
        return x + y;
    }
    static double plusMethod(double x, double y){
        return x + y;
    }
    public static void main(String[] args) {
        int myNum1 = plusMethod(5, 10);
        double myNum2 = plusMethod(6.3, 7.23);
        System.out.println(myNum1);
        System.out.println(myNum2);
    }
}
