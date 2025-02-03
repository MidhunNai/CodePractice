package Practice;

public class Practice{

    public static String replaceLeadingZero(String str) {
        String result = str.replaceFirst("^0+", "");
        return result.isEmpty() ? "0" : result;
    }

    public static void main(String[] args) {
        String str = "00000000abcdefghijklmnopqrstuvwxyz";
        String str1 = "abjfdlhsd";
        String removedZero = replaceLeadingZero(str);
        System.out.println(removedZero);
        System.out.println(str.equals(str1));
    }
}