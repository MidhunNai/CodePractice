import java.util.Scanner;

public class JavaBasic2 {
    //Write a program to swap two number
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int m;
        int n;
        System.out.println("Enter first number m = ");
        m = s.nextInt();
        System.out.println("Enetr secon numner n = ");
        n = s.nextInt();
        int temp = m;
        m = n;
        n = temp;

        System.out.println("Value of m = "+ m);
        System.out.println("Value of n = "+n);
        s.close();
    }
}
