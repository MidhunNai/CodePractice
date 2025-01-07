// Program for factorial of a number

import java.util.Scanner;

public class P12 {
    public static void main(String[] args) {
        System.out.println("Enter an number");
        Scanner s = new Scanner(System.in);
        int num = s.nextInt();
        long factorial = 1;
        for(int i = num; i > 0; i--) {
            factorial = i * factorial;
        }
        System.out.println("Factorial of given number is "+ factorial);
        s.close();
    }
}