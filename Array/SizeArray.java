public class SizeArray {
    public static void main(String[] args) {
        int arr[] = {20, 40, 60, 80, 100};

        //Access Array Elements
        System.out.println(arr[0] +"");

        //Update Array Elements
        arr[0] = 120;
        System.out.println(arr[0] +"");

        //Traverse on Array
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            System.out.println(arr[i] +"");
        }

        //Size of Array
        System.out.println("Size of Array : " +n );
    } 
}
