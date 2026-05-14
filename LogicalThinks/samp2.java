import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter student name: ");
        String name = sc.nextLine();

        System.out.print("Enter marks: ");
        int marks = sc.nextInt();

        System.out.println("Student Name: " + name);
        System.out.println("Marks: " + marks);

        if (marks >= 50) {
            System.out.println("Result: Pass");
        } else {
            System.out.println("Result: Fail");
        }

        for (int i = 1; i <= 3; i++) {
            System.out.println("Welcome " + name);
        }

        sc.close();

    }
    int total = 500;
int discount = 50;
int finalAmount = total - discount;

System.out.println("Total Amount: " + total);
System.out.println("Discount: " + discount);
System.out.println("Final Amount: " + finalAmount);

if (finalAmount > 400) {
    System.out.println("Premium Customer");
} else {
    System.out.println("Regular Customer");
}

System.out.println("Thank You");
System.out.println("Visit Again");
}
