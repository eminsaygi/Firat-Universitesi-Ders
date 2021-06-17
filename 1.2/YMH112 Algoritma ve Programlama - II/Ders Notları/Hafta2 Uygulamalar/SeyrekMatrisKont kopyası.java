package seyrekmatriskont;

import java.util.Scanner;

public class SeyrekMatrisKont {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Matrisin boyutlarını giriniz: ");
        int m = sc.nextInt();
        int n = sc.nextInt();
        double[][] mat = new double[m][n];
        int zeros = 0;
        System.out.println("Matrisin elemanlarını giriniz: ");
        for(int i=0; i<m; i++)
        {
            for(int j=0; j<n; j++)
            {
                mat[i][j] = sc.nextDouble();
                if(mat[i][j] == 0)
                {
                    zeros++;
                }
            }
        }
 
        if(zeros > (m*n)/2)
        {
            System.out.println("Girilen matris seyrek matristir");
        }
        else
        {
            System.out.println("Girilen matris seyrek matris değildir");
        }
 
        sc.close();
    }
    
}
