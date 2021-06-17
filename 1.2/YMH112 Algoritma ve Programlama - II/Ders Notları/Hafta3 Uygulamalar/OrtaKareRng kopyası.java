package ortakarerng;

import java.util.Random;
import java.util.Scanner;

public class OrtaKareRng {

    static int a[] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000};
    
    static int Uret(int numb, int dig)
    {
        int sqn = numb*numb, next_num=0;
        int trim = (dig/2);
        sqn = sqn / a[trim];
        for(int i=0; i<dig; i++)
        {
            next_num += (sqn%(a[trim]))*(a[i]);
            sqn = sqn/10;
        }
        return next_num;
    }
    
    public static void main(String[] args) {
        System.out.println("İstediğiniz rasgele sayının basamak sayısını giriniz: ");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
 
        int ilk=1, son=1;
 
        ilk = a[n-1];
        son = a[n]; 
 
        Random rand = new Random();
        int sayi = rand.nextInt(son-ilk)+ilk;
        System.out.print("Rasgele Sayılar:\n" +sayi+", ");
        //int yeni_sayi=0;
        for(int i=0; i<9; i++)
        {
            sayi = Uret(sayi, n);
            System.out.print(sayi+", ");
        }
        System.out.print("...");
 
        sc.close();
    }
    
}
