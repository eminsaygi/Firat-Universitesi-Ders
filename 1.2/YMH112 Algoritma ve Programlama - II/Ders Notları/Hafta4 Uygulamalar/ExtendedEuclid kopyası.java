package extendedeuclid;

import java.util.Scanner;

public class ExtendedEuclid {

    public void hesapla(long a, long b)
    {
        long x = 0, y = 1, xyeni = 1, yyeni = 0, gecici;
        while (b != 0)
        {
            long q = a / b;
            long r = a % b;
 
            a = b;
            b = r;
 
            gecici = x;
            x = xyeni - q * x;
            xyeni = gecici;
 
            gecici = y;
            y = yyeni - q * y;
            yyeni = gecici;            
        }
        System.out.println("Kökler  x : "+ xyeni +" y :"+ yyeni);
    }
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Extended Euclid Algoritması Testi\n");
        /** Make an object of ExtendedEuclid class **/
        ExtendedEuclid ee = new ExtendedEuclid();
 
        /** Accept two integers **/
        System.out.println("a ve değerlerinin giriniz ax + by = obeb(a, b)\n");
        long a = scan.nextLong();
        long b = scan.nextLong();
        ee.hesapla(a, b);    
    }
    
}
