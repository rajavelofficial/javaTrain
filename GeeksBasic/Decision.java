import java.util.Scanner;

public class Decision {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.println("Rakshan being with Phone? (yes(1) or no(0)) :");
        int value = sc.nextInt();
        int answer = 0;


        if(answer == value)
        {
            System.out.println("Rakshan Study Well");
        }else{
            System.out.println("Rakshan, Not Study. 90 % percentage No Chance.");
        }
    }
    
}
