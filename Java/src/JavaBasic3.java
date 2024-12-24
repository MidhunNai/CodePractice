import java.util.Scanner;

public class JavaBasic3 {
    // Programm to add two integer
    public static void main(String[] args) {
        System.out.println("Enter first number, a =");
        Scanner s = new Scanner(System.in);
        int a = s.nextInt();
        System.out.println("Enter another number, b=");
        int b = s.nextInt();
        int sum = a + b;
        System.out.println("Sum of two integer is "+ sum);
        s.close();
    }
}
