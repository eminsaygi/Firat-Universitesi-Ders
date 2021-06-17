package dosyaıslemleri;

import java.io.File;
import java.io.FileOutputStream;

import java.io.FileNotFoundException;
import java.util.Scanner;

public class DosyaIslemleri {
    
    public static void DosyaYaz(String veri)
    {
        File file=new File("/Users/fatihozkaynak/Desktop/testDosya2.txt");   
        try 
        {
            //FileOutputStream dosya=new FileOutputStream(file);
            FileOutputStream dosya=new FileOutputStream(file,true);
            dosya.write(veri.getBytes());
            dosya.flush();
            dosya.close();
        } 
        catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    public static void DosyaOku()
    {
        File file=new File("/Users/fatihozkaynak/Desktop/lisp başlangıç kodlar.txt");
		
        try 
        {
            Scanner sc=new Scanner(file);
            while(sc.hasNextLine()){
                System.out.println(sc.nextLine());
            }
            sc.close();
        } 
        catch (FileNotFoundException e) {
        e.printStackTrace();
        }
    }
    
    public static void main(String[] args) {
        DosyaYaz(" dünya");
        
        DosyaOku();
    }
}
