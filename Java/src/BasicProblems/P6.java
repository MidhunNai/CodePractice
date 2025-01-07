// Find odd or even integer

import java.util.Scanner;

public class P6 {
    public static void main(String[] args) {
        System.err.println("Enter an integer!");
        Scanner s = new Scanner(System.in);
        int num = s.nextInt();
        if ( num%2 == 0 ) {
            System.err.println("Given number is Even");
        } else if ( num%2 != 0 ) {
            System.err.println("Given number is Odd ");
        } else {
            System.err.println("Invalid number :(");
        }
        s.close();
    }
}
