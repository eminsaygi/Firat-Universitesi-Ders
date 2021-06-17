package euclidgcd;

import java.util.Scanner;

public class EuclidGCD {

    public long obeb(long p, long q)
    {
        if (p % q == 0)
            return q;
        return obeb(q, p % q);
    }
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Euclid GCD Algoritması Test\n");
        /** Make an object of EuclidGcd class **/
        EuclidGCD nesne = new EuclidGCD();
 
        /** Accept two integers **/
        System.out.println("İki sayı değeri giriniz\n");
        long n1 = scan.nextLong();
        long n2 = scan.nextLong();
        /** Call function gcd of class EuclidGcd **/
        long gcd = nesne.obeb(n1, n2);
        System.out.println("\n"+ n1 +" ve "+ n2 +"'nin OBEB değeri = "+ gcd);
    }
    
}
