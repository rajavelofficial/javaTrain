public class JavaPrecedence {
    public static void main(String[] args) {

        int a =10, b = 5, c =2 ;
        int result = a + b - c;           //Left-to-Right Precedence (a + b) - c
        
        int d, e ;
        int RTL = d = e = 2 ;             //Right-to-Left Precedence d = (e = 2)

        int HighertoLower = a + b * c / d - e;     //Higher-to-Lower Precedence




        System.out.println(result);
        System.out.println(RTL);
        System.out.println(HighertoLower);


    }
    
}
