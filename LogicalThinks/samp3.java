import java.util.Scanner;

public class samp3 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int num = sc.nextInt();

        boolean isPrime = true;

        if (num <= 1) {
            isPrime = false;
        } else {

            for (int i = 2; i <= num / 2; i++) {

                if (num % i == 0) {
                    isPrime = false;
                    break;
                }
            }
        }

        if (isPrime) {
            System.out.println(num + " is a Prime Number");
        } else {
            System.out.println(num + " is not a Prime Number");
        }

        sc.close();
    }
    public class HelloWorld {
    public static void main(String[] args) {

        int a = 10;
        int b = 20;
        int sum = a + b;

        System.out.println("First Number: " + a);

        System.out.println("Second Number: " + b);

        System.out.println("Sum = " + sum);

        System.out.println("Java Program Example");
    }
}
}