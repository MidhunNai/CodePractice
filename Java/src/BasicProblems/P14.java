// Program to Calculate Simple Interest


import java.util.Scanner;



public class P14 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter Principal amount:");
        int p = scanner.nextInt();
        System.out.println("Enter years:");
        int t = scanner.nextInt();
        System.out.println("Enter rate of intrest:");
        double r = scanner.nextDouble();
        scanner.close();

        double simpleIntrest = (p * t * r) / 100 ;

        System.out.println("Simple intrest for given principal amount is "+simpleIntrest);

    }
}