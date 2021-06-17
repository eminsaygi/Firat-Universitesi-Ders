package pollardrho;

import java.util.Scanner;

public class PollardRho {

    private static final long C = 1; 
    
    private long f(long X)    
    {
        return X * X + C;
    }
    
    private long rho(long N) 
    {
        long x1 = 2, x2 = 2, bolen;        
        if (N % 2 == 0) 
            return 2;
        do 
        {
            x1 = f(x1) % N;
            x2 = f(f(x2)) % N;
            bolen = obeb(Math.abs(x1 - x2), N);
        } while (bolen == 1);
        
        return bolen;
    }
    
    public  long obeb(long p, long q)
    {
        if (p % q == 0)
            return q;
        return obeb(q, p % q);
    }
    
    public boolean asalKontrol(long N)
    {
        for (int i = 2; i <= Math.sqrt(N); i++)
            if (N % i == 0)
                return false;
        return true;
    }
    
    public void factor(long N) 
    {
        if (N == 1)
            return;
        if (asalKontrol(N)) 
        {
            System.out.println(N); 
            return; 
        }
           
        long bolen = rho(N);
        factor(bolen);
        factor(N / bolen);
    }
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Pollard Rho Algorithm\n");                
        System.out.println("Bir sayı Giriniz");
        long N = scan.nextLong();
        System.out.println("\nÇarpanlar : ");
        PollardRho pr = new PollardRho();
        pr.factor (N);    
    }
    
}
