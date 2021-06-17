package carpanlarinaayir;

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class CarpanlarinaAyir {

    static Set asalCarpanlar(long number) 
    {
        long kopya = number, i;
	Set asalCarpan = new HashSet<>();
        for (i = 2; i <= kopya; i++) 
        {
            if (kopya % i == 0) 
            {
                asalCarpan.add(i);
                kopya /= i;
                i--;
            }
        }
        return asalCarpan;
    }
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        long n;
        System.out.println("Sayı giriniz: ");
        n = input.nextLong();
        System.out.println("\n" + n + "'in asal çarpanları: " + asalCarpanlar(n));
    }
    
}
