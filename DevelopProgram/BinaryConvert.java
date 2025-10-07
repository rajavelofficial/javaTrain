import java.util.Scanner;

public class BinaryConvert {
    public static void main(String[] args) {
        Scanner value = new Scanner(System.in);
        System.out.print("Enter the number you want to convert as Binary Value : ");
        int FirstValue = value.nextInt();

        String second = "";
        int First = FirstValue;

        while( First > 0 ){
            second = (First % 2) + second;
            First = First / 2;
        }
        System.out.print("Binary value is : ");
        System.out.println(second);
        
    }
    
}
