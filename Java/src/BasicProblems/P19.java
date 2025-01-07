
// Program to Print Pyramid Number Pattern

public class P19 {
    public static void main(String[] args) {
        // print decresing spaces
        // print number
        int n = 5;
        for (int i = 1; i <= n; i++) {
            // Print spaces
            for (int j = 1; j <= n - i; j++) {
                System.out.print(" ");
            }

            // Print numbers
            for (int k = 1; k <= i; k++) {
                System.out.print(k + " ");
            }

            // Move to the next line
            System.out.println();
        }
    }
}
