// Program to Print Reverse Pyramid Star Pattern

public class P20 {
    public static void main(String[] args) {
        int n = 7;
        for (int i = 0; i < n; i++) {
            for(int j = 0; j < i; j++){
                System.out.print(" ");
            }
            for(int k = 0; k < (2 * (n - i) - 1); k++) {
                System.out.print("*");
            }
            System.out.println();
        }
        
    }
}
