// Program to Find Sum of Fibonacci Series Numbers of First N Even Indexes

/* Steps to write this
1. Find N even index with 2N - 2
2. Store two preceding fibonacci numbers and calculate the next number
3. Track the index whie iterating and add the number on the even index place.
*/

import java.util.Scanner;

public class P13 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter an integer: ");
        int n = scanner.nextInt();
        if (n <= 0) {
            System.out.println("Invalid Input");
        }

        int sum = 0;
        int a = 0;
        int b = 1;
        int index = 0;
        int evenCount = 0;

        while (evenCount < n) {
            if (index % 2 == 0) {
                sum += a;
                evenCount++;
            }
            int next = a + b;
            a = b;
            b = next;
            index++;
        }
        System.err.println("Sum of Fibonacci at first " + n + " even index: " + sum);
    }
}