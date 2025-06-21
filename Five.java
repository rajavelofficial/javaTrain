public class Five{
    public static void main(String[] args) {
        String[] crypto = {"Bitcoin", "BinanceSmartChain", "Floki", "Sominia", "Doge"};
        crypto[1] = "Ethereum";
        System.out.println("Total Coins In Array :  " +crypto.length);
        System.out.println(crypto[0]);
        System.out.println(crypto[1]);
        
    }
}