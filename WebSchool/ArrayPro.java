public class ArrayPro {
    public static void main(String[] args) {
        int ages[]= {21, 23, 25, 34, 37, 48, 27};

        int length = ages.length;
        float lowest = ages[1];
        int sum = 0;

        for (int age : ages){
            sum += age;
        }
          int average = sum/length;
        System.out.println("The Average Age is :  " +average);

        for(int age : ages){
            if(age<lowest){
                lowest = age;
            }
        }
        System.out.println("The Minimum Age is : " + lowest);


    }
}
