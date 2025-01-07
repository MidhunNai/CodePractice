// Program to revese a string

package StringProblems;

public class P3 {
    public static void main(String[] args) {
        String str = "MidhunNair";
        StringBuilder reversed = new StringBuilder(str);
        String reversedString = reversed.reverse().toString();
        System.out.println(reversedString);
    }
}
