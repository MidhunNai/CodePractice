import java.util.Scanner;

public class JavaBasic1 {
    public static void main(String[] arg) {
        //Program to get int value from user and print it
        int num;
        System.out.println("Enter any integer: ");
        Scanner s = new Scanner(System.in);
        num = s.nextInt();
        System.out.println("You have entered: "+ num);
        s.close();
    }
}
