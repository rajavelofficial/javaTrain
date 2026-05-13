import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter first number: ");
        int a = sc.nextInt();

        System.out.print("Enter second number: ");
        int b = sc.nextInt();

        int sum = a + b;
        int sub = a - b;
        int mul = a * b;

        System.out.println("Addition: " + sum);
        System.out.println("Subtraction: " + sub);
        System.out.println("Multiplication: " + mul);

        if (b != 0) {
            System.out.println("Division: " + (a / b));
        } else {
            System.out.println("Division not possible");
        }

        System.out.println("Program Finished");
    }
}