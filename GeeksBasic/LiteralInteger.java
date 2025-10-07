
public class LiteralInteger {
    public static void main(String[] args) {

        //Literal Integers
        int Decimal = 2003;

        int Octal = 0100;

        int Binary = 0b1111 ;

        int HexaDecimal = 0x2934f342 ;

        //Literal Floating points

        float a = 122.230f;
        float b = 0123.212f;

        //Char Literals

        char one = 'R';
        char two = 061;
        char unicode = '\u0035'; // The final output of the char is R15, Yamaha bike model

        //String Literals

        String text = "This is a String literal \n"

            + "which spans not one and not two\n"

            + "but three lines of text.\n";

        String val = "Hello World!";
        
        System.out.println(val);
        System.out.println(text);


        System.out.print(one);
        System.out.print(two);
        System.out.println(unicode); 

        System.out.println(a);
        System.out.println(b);

        System.out.println("Decimal Value : " +Decimal);
        System.out.println("Octal Value : " +Octal);
        System.out.println("Binary Value : " +Binary);
        System.out.println("HexaDecimal Value : " +HexaDecimal);
    }
    
}
