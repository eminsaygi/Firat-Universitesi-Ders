package okek;
import java.util.Scanner;

public class Okek {

    static int okek1(int x, int y){ 
        int okek=0; 
        for(int i=1; i<=x*y; i++){ 
            if(i%x==0 && i%y==0){ 
                okek=i; 
                break; 
            } 
        }        
        return okek; 
    }
    
    static int obeb1(int x, int y)
    {
        return (x*y)/okek1(x,y);
    }
    
    static int obeb2(int x, int y)
    {
        int r=0, a, b;
        a = (x > y) ? x : y; // a daha büyük sayıdır
        b = (x < y) ? x : y; // b daha küçük sayıdır
 
        r = b;
        while(a % b != 0)
        {
            r = a % b;
            a = b;
            b = r;
        }
        return r;
    }
    
    static int okek2(int x, int y)
    {
        int a;
        a = (x > y) ? x : y; // a daha büyüktür
        while(true)
        {
            if(a % x == 0 && a % y == 0)
                return a;
            ++a;
        }	
    }
    
    public static void main(String[] args) {
        int x, y; 
        System.out.print("Birinci sayıyı giriniz: "); 
        Scanner oku=new Scanner(System.in); 
        x=oku.nextInt(); 
        System.out.print("İkinci sayıyı giriniz: "); 
        y=oku.nextInt(); 
        
        System.out.println("Yöntem 1 için OKEK: "+okek1(x,y));
        System.out.println("Yöntem 1 için OBEB: "+obeb1(x,y));
        System.out.println("Yöntem 2 için OKEK: "+okek2(x,y));
        System.out.println("Yöntem 1 için OBEB: "+obeb2(x,y));
    }
    
}
