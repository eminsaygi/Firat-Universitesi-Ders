package strassencarpimalg;

import java.util.Scanner;

public class StrassenCarpimAlg {

    public int[][] carp(int[][] A, int[][] B)
    {        
        int n = A.length;
        int[][] R = new int[n][n];
        /** tümevarım için temel durum **/
        if (n == 1)
            R[0][0] = A[0][0] * B[0][0];
        else
        {
            int[][] A11 = new int[n/2][n/2];
            int[][] A12 = new int[n/2][n/2];
            int[][] A21 = new int[n/2][n/2];
            int[][] A22 = new int[n/2][n/2];
            int[][] B11 = new int[n/2][n/2];
            int[][] B12 = new int[n/2][n/2];
            int[][] B21 = new int[n/2][n/2];
            int[][] B22 = new int[n/2][n/2];
 
            /** A matrisi 4 parçaya bölümüyor **/
            parcala(A, A11, 0 , 0);
            parcala(A, A12, 0 , n/2);
            parcala(A, A21, n/2, 0);
            parcala(A, A22, n/2, n/2);
            
            /** B matrisi 4 parçaya bölümüyors **/
            parcala(B, B11, 0 , 0);
            parcala(B, B12, 0 , n/2);
            parcala(B, B21, n/2, 0);
            parcala(B, B22, n/2, n/2);
 
            /** 
              M1 = (A11 + A22)(B11 + B22)
              M2 = (A21 + A22) B11
              M3 = A11 (B12 - B22)
              M4 = A22 (B21 - B11)
              M5 = (A11 + A12) B22
              M6 = (A21 - A11) (B11 + B12)
              M7 = (A12 - A22) (B21 + B22)
            **/
 
            int [][] M1 = carp(topla(A11, A22), topla(B11, B22));
            int [][] M2 = carp(topla(A21, A22), B11);
            int [][] M3 = carp(A11, fark(B12, B22));
            int [][] M4 = carp(A22, fark(B21, B11));
            int [][] M5 = carp(topla(A11, A12), B22);
            int [][] M6 = carp(fark(A21, A11), topla(B11, B12));
            int [][] M7 = carp(fark(A12, A22), topla(B21, B22));
 
            /**
              C11 = M1 + M4 - M5 + M7
              C12 = M3 + M5
              C21 = M2 + M4
              C22 = M1 - M2 + M3 + M6
            **/
            int [][] C11 = topla(fark(topla(M1, M4), M5), M7);
            int [][] C12 = topla(M3, M5);
            int [][] C21 = topla(M2, M4);
            int [][] C22 = topla(fark(topla(M1, M3), M2), M6);
 
            /** 4 parça sonuç matrisi içerisinde birleştirilir **/
            birlestir(C11, R, 0 , 0);
            birlestir(C12, R, 0 , n/2);
            birlestir(C21, R, n/2, 0);
            birlestir(C22, R, n/2, n/2);
        }
        /** return sonuç **/    
        return R;
    }
    
    /** iki matrisin farkını hesaplayan fonksiyon **/
    public int[][] fark(int[][] A, int[][] B)
    {
        int n = A.length;
        int[][] C = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                C[i][j] = A[i][j] - B[i][j];
        return C;
    }
    
    /** iki matrisin toplamını hesaplayan fonksiyon **/
    public int[][] topla(int[][] A, int[][] B)
    {
        int n = A.length;
        int[][] C = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                C[i][j] = A[i][j] + B[i][j];
        return C;
    }
    
    /** Matrisi daha küçükparçalara ayıran fonksiyon **/
    public void parcala(int[][] P, int[][] C, int iB, int jB) 
    {
        for(int i1 = 0, i2 = iB; i1 < C.length; i1++, i2++)
            for(int j1 = 0, j2 = jB; j1 < C.length; j1++, j2++)
                C[i1][j1] = P[i2][j2];
    }
    
    /** küçük parçaları birleştiren fonksiyonx **/
    public void birlestir(int[][] C, int[][] P, int iB, int jB) 
    {
        for(int i1 = 0, i2 = iB; i1 < C.length; i1++, i2++)
            for(int j1 = 0, j2 = jB; j1 < C.length; j1++, j2++)
                P[i2][j2] = C[i1][j1];
    }
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Strassen Çarpım Algoritması Testi\n");
        
        /** Sınıfın bir nesnesini oluşturuyoruz **/
        StrassenCarpimAlg s = new StrassenCarpimAlg();
 
        System.out.println("Matrisin taban değerini giriniz :");
        int N = scan.nextInt();
        
        System.out.println("Birinci matris için" + N + ". derecen bir matris giriniz\n");
        int[][] A = new int[N][N];
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                A[i][j] = scan.nextInt();
 
        System.out.println("İkinci matris için" + N + ". derecen bir matris giriniz\n");
        int[][] B = new int[N][N];
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                B[i][j] = scan.nextInt();
 
        int[][] C = s.carp(A, B);
 
        System.out.println("\nSonuç : ");
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
                System.out.print(C[i][j] +" ");
            System.out.println();
        }
    }
    
}
