// Program to Print Right Triangle Star Pattern

public class P17 {
    public static void main(String[] args) {
        int n = 5;
        for(int i = 1; i <= n; i++){
            for(int y = 1; y <= i; y++){
                System.out.print("*");
            }
            System.out.println(" ");
        }
    }
}
