
import java.util.Scanner;

public class FizzBuzz {
    // Dec 12,2025, 22:45
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int number = sc.nextInt();

        if(number % 3 == 0 && number % 5 == 0){
            System.out.println("FizzBuzz");
        }else if(number % 3 == 0){
            System.out.println("Fizz");
        }else if(number % 5 == 0){
            System.out.println("Buzz");
        }else{
            System.out.println(number);
        }
    }
    
}
