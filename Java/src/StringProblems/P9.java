//check if one string is substring of another

package StringProblems;

public class P9 {
    public static void main(String[] args) {
        String s1 = "abcde";
        String s2 = "bc";
        boolean res = s1.contains(s2);
        System.out.println(res);
    }
}
