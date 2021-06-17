package captchauretimi;

// Dışarıdan grilen değer m ise 
// bu program m! adet ve m uzunluğundan captcha üretir
// captcha değerleri 0-9 arasında değişen rakamlardır

import java.util.Random;
import java.util.Scanner;

public class CaptchaUretimi {

    static void permute(int []a, int k)
    {
        if(k==a.length)
        {
            for(int i=0; i<a.length; i++)
            {
                System.out.print(a[i]);
            }
            System.out.println();	
        }
        else
        {
            for (int i = k; i<a.length; i++) 
            {
                int gecici=a[k];
                a[k]=a[i];
                a[i]=gecici;
 
                permute(a,k+1);
 
                gecici=a[k];
                a[k]=a[i];
                a[i]=gecici;
            }
        }	
 
    }
    
    public static void main(String[] args) {
        System.out.println("Oluşturulacak CAPTCHA uzunluğunu giriniz: ");
        Scanner klavye = new Scanner(System.in);
        int m = klavye.nextInt();
        Random random = new Random();
        int []a = new int[m];
        for(int i=0; i<m; i++)
        {
            a[i] = random.nextInt(10);
        }
 
        System.out.println("Olası CAPTCHA değerleri: ");
        permute(a, 0);
 
        klavye.close();
    }
    
}
