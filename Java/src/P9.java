
import java.util.Scanner;

// Program to Display All Prime Numbers from 1 to N

public class P9 {
    public static void main(String[] args) {
        System.err.println("Enter any number!");
        Scanner s = new Scanner(System.in);
        int num = s.nextInt();
        int flg;
        int x, y;
        for (x = 1; x<= num; x++) {
            if ( num == 0 || num == 1) {
                continue;
            }
            flg = 1;
            for (y = 2; y<= x/2 ; ++y) {
                if (x%y == 0) {
                    flg = 0;
                    break;
                }
            }
            if (flg == 1)
                System.out.print(x + " ");
        }
    }
}
