package rasgelesayiuretimi;

import java.util.Random;
import java.util.Scanner;

public class RasgeleSayiUretimi {

    public static void main(String[] args) {
        Random rand = new Random();
        Scanner sc = new Scanner(System.in);
        System.out.println("Rasgele sayıların başlangıç ve bitiş aralığını giriniz: ");
        int ilk = sc.nextInt();
        int son = sc.nextInt();
 
        System.out.println("Kaç tane rasgele sayı üretmek istiyorsunuz: ");
        int adet = sc.nextInt();
        
        for(int i=0; i<adet; i++)
        {
            System.out.print(rand.nextInt(son-ilk+1)+ilk + ", ");
        }
        System.out.print("...");
        sc.close();
    }
    
}
