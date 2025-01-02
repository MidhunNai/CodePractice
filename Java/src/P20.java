// Program to Print Reverse Pyramid Star Pattern

public class P20 {
    public static void main(String[] args) {
        int n = 5;
        for (int i = 1; i <= n; i++) {
            for ( int j = 1; j <= n; j++) {
                System.out.print("*");
            }
            for ( int j = 1; j <= n - 1; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
        
    }
}
