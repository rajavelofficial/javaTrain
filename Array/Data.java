public class Data {
    public void primitive(){
        int[] arr = {10, 20, 30, 40};
        int n = arr.length;
        
        System.err.println("Primitive Type:");
        System.out.println(" ");
        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println("");
        System.err.println("");

        System.out.println("No Primitive Type:");
        System.out.println("");
        String[] name = {"Raja", "Ram", "Raju"};
        for (int j = 0; j < name.length; j++) {
            System.err.print(name[j] +" ");
            
        }
    }
    public static void main(String[] args) {
        Data Obj = new Data();
        Obj.primitive();
    }
}
