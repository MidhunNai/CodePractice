//Program to Find if a Given Year is a Leap Year

public class P10 {
    static boolean leapYear = false;
    public static void isLeapYear(int year) {
        if(year % 4 == 0){
            if (year % 100 == 0){
                if(year % 400 == 0){
                    leapYear = true;
                } else {
                    leapYear = false;
                }
            } else {
                leapYear = true;
            }
        } else {
            leapYear = false;
        }
    }
    public static void main(String[] args) {
        int year = 2000;
        isLeapYear(year);
        if(leapYear) 
            System.out.println("Given year is a leap year.");
        else 
            System.out.println("Given year is not a leap year.");
    }
}
