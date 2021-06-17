package rasgelehexadecimalbyte;

import java.util.Random;

public class RasgeleHexadecimalByte {

    public static void main(String[] args) {
        Random rasgele = new Random();
        int deger = rasgele.nextInt();
        String Hex = "";
        Hex = Integer.toHexString(deger);
        System.out.println("Rasgele Hex Byte: " + Hex);
    }
    
}
