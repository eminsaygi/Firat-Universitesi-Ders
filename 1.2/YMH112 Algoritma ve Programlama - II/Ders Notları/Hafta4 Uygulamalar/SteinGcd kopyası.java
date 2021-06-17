package steingcd;

import java.util.Scanner;

public class SteinGcd {

    public int obeb(int u, int v)
    {
        int kaydir;
        if (u == 0)
            return v;
        if (v == 0)
            return u;
        for (kaydir = 0; ((u | v) & 1) == 0; ++kaydir) 
        {
            u >>= 1;
            v >>= 1;
        }
        while ((u & 1) == 0)
            u >>= 1;
        do 
        {
            while ((v & 1) == 0)  
                v >>= 1;
 
            if (u > v) 
            {
                int t = v; 
                v = u; 
                u = t;
            }  
            v = v - u;                      
        } while (v != 0);
 
        return u << kaydir; 
    }
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Stein GCD Algoritmasi Test\n");
        /** Make an object of SteingGcd class **/
        SteinGcd sg = new SteinGcd();
 
        System.out.println("iki sayi giriniz\n");
        int n1 = scan.nextInt();
        int n2 = scan.nextInt();
        /** Call function gcd of class SteinGcd **/
        int gcd = sg.obeb(n1, n2);
        System.out.println("\n"+ n1 +" ve "+ n2 +"'nin OBEB degeri = "+ gcd);
    }
    
}
