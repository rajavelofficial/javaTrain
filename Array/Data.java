public class Data {
    public void primitive(){
        int[] arr = {10, 20, 30, 40};
        int n = arr.length;
        int total = 0;
        
        System.err.print("Primitive Type: ");
        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " + ");
            total += arr[i];
        }
        System.out.print(" = " +total);
        System.out.println("");

        System.out.print("No Primitive Type: ");
        String[] name = {"Raja,", "Ram,", "Raju"};
        for (int j = 0; j < name.length; j++) {
            System.err.print(name[j] +" ");
            
        }
    }
    public static void main(String[] args) {
        Data Obj = new Data();
        Obj.primitive();
    }
}
