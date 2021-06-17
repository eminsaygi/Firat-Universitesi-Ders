package fisheryatesdizikarma;

import java.util.Random;
import java.util.Scanner;

public class FisherYatesDiziKarma {

    static int[] fisherYatesKaristir(int []arr, int n)
    {
        int []a = new int[n];
        int []ind = new int[n];
        for(int i=0; i<n; i++)
            ind[i] = 0;
        int index;
        Random rand = new Random();
        for(int i=0; i<n; i++)
        {
            do
            {
                index = rand.nextInt(n);
            } 
            while(ind[index] != 0);
 
            ind[index] = 1;
            a[i] = arr[index];
        }
        return a;
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Dizi boyutunu giriniz: ");
        int n = sc.nextInt();
        int []a = new int[n];
        int []res = new int[n];
        
        System.out.println("Dizinin elemanlarını giriniz: ");
        for(int i=0; i<n; i++)
        {
            a[i] = sc.nextInt();
        }
        
        res = fisherYatesKaristir(a, n);
        System.out.println("Karıştırılan dizinin elemanları: ");
        for(int i=0; i<n; i++)
        {
            System.out.print(res[i]+" ");
        }
        
        sc.close();
    }
}
