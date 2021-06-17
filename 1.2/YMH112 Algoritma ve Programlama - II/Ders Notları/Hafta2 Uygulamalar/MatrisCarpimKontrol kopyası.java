package matriscarpimkontrol;

import java.util.Scanner;

public class MatrisCarpimKontrol {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Birinci matrisin boyutlarını giriniz:\n ");
        int satirA = sc.nextInt();
        int sutunA = sc.nextInt();
 
        System.out.println("İkinci matrisin boyutlarının giriniz:\n ");
        int satirB = sc.nextInt();
        int sutunB = sc.nextInt();
 
        if(sutunA == satirB)
        {
            System.out.println("Matrisler çarpılabilir");
        }
        else
        {
            System.out.println("Matrisler çarpılamaz");
        }
        sc.close();
    }
    
}
