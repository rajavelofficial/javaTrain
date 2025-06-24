public class Multidimension {
    public static void main(String[] args) {
        String[][] cryptoCoin = {{"Bitcoin", "Ethereum", "Binance"}, {"Floki", "Doge", "Game7"}};
        cryptoCoin[1][0] = "Beam";   //Floki meme token cheged to Beam token
        System.out.println(cryptoCoin [1][0]);
    }
    
}
