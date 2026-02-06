class Employee{
    int id_no ;
    String name;

    public Employee(int id_no, String name) {
        this.id_no = id_no ;
        this.name = name;
    }
}
public class ArrayObjects {
    public static void main(String[] args) {

        Employee[] arr;

        arr = new Employee[5];

        arr[0] = new Employee(1, "ChatGPT");
        arr[1] = new Employee(2, "Google Gemini");
        arr[2] = new Employee(3, "DeepSeek");
        arr[3] = new Employee(4, "Sweat Ai");
        arr[4] = new Employee(5, "Gork.ai");

        int n = arr.length;

        System.out.println("Hiring new Employe for Company and The list of Employee:");
        for (int i = 0; i < n; i++) {
            System.err.println("Employe Name : " +arr[i].id_no +" - " +arr[i].name);
        }

    }
    
}
