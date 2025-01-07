// Program to Print Mirror Upper Star Triangle Pattern
/*
      * 
     * * 
    * * * 
   * * * * 
  * * * * * 
 * * * * * * 
* * * * * * * 
* * * * * * * 
 * * * * * * 
  * * * * * 
   * * * * 
    * * * 
     * * 
      * 
 */

public class P21 {
    public static void main(String[] args) {
        int n = 7;
        // For upper trianle
        // for (int i = 0; i < n; i++) {
        //     for (int j = 1; j < n - i; j++) {
        //         System.out.print(" ");
        //     }
        //     for (int k = 0; k <= i; k++) {
        //         System.out.print("* ");
        //     }
        //     System.out.println();
        // }
        // // For Lower Trianle
        // for (int i = 0; i < n; i++) {
        //     for (int j = 0; j < i; j++) {
        //         System.out.print(" ");
        //     }
        //     for (int k = 1; k <= n - i; k++) {
        //         System.out.print("* ");
        //     }
        //     System.out.println();
        // }
        for (int i = 0; i < 2 * n; i++) {
            int spaces = Math.abs(n - i - 1);
            int stars = n - spaces;

            // Print spaces
            for (int j = 0; j < spaces; j++) {
                System.out.print(" ");
            }

            // Print stars
            for (int k = 0; k < stars; k++) {
                System.out.print("* ");
            }

            System.out.println();
        }
    }
}
