
import java.util.Scanner;

public class Star {
    public static void main(String[] args){
        Scanner one = new Scanner(System.in);
        System.out.println("Enter any Integer Value to Get Star Triangle :");
        int n=one.nextInt();
        for (int i = 1; i <= n; i++) {
            System.err.println("");
            for(int j = 1; i >= j; j++ ){
                System.out.print("*");
            }
        }
    }
    
}
