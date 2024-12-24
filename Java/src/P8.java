//Program to Find LCM of Two Numbers

public class P8 {
    public static void main(String[] args) {
        int a = 15;
        int b = 25;
        int largest = a > b ? a : b;
        while( true ) {
            if (largest % a == 0 && largest % b ==0 )
                break;
            largest++;
        }
        System.err.println("LCM of given number is "+ largest);
    }
}
