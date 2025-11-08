import java.util.Scanner;

public class LeafYear {
    public static void main(String[] args) {
        Scanner Year = new Scanner(System.in);

        System.out.println("LeafYear or Not ");
        System.out.print("Enter the Year : ");
        int Leaf = Year.nextInt();

        int Value = Leaf % 4;

        if(Value <= 0)
        System.out.println(Leaf +" is Leaf Year.");
        else
        System.out.println(Leaf +" is Not a Leaf Year.");
    }
    
}
