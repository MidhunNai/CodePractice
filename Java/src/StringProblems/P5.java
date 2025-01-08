// Check if a String “StartsWith” Another String

package StringProblems;

public class P5 {
    public static void main(String[] arg) {
        String s = "Hello world";
        String prefix = "Hello";
        if(s.startsWith(prefix)) {
            System.out.println("The strint starts with " + prefix);
        } else {
            System.out.println("The string does not start with " + prefix);
        }
    }
}
