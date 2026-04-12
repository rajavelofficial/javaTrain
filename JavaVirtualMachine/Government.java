class HighwayBill{
    String color, carName;
    int carSpeed;

    void carDetails(){
        System.out.println("The " + color + " Color " + carName + " Super Car Hiting " + carSpeed +" km/h ECR Highway Bill That Car ");
    }
}
    public class Government{
        public static void main(String[] args) {
            HighwayBill bill = new HighwayBill();
            bill.carName = "TATA";
            bill.color = "Black";
            bill.carSpeed = 200;
            bill.carDetails();
        }
}

