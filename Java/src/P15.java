// Program for compound interest

public class P15 {
    public static void main(String[] args) {
        int p = 1200;
        double t = 2;
        double r = 5.4;
        double compountIntrest = p * (Math.pow((1 + r/100), t));
        System.out.println("The compound intrest of given principal amount is "+ compountIntrest);
    }
}
