// Program to remove spaces from start and end

package StringProblems;

public class P6 {
    public static void main(String[] args) {
        String s = "    Hello Midhun    ";
        String trimmedString = s.stripLeading().stripTrailing();
        System.out.println(trimmedString);
    }
}
