//Find Largest Among 3 Numbers

public class P7 {
    static int lasgestOfThree (int a, int b, int c) {
        return c > (a > b ? a : b) ? c : ((a > b) ? a : b);
    }
   public static void main(String[] args) {
        int a, b, c;
        int largest;
        a = 5;
        b = 3;
        c = 8;
        largest = lasgestOfThree(a, b, c);
        System.out.println("The largest number is "+ largest);
   } 
}
