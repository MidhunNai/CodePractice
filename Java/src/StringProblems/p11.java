//Program to Replace Characters of a String

package StringProblems;

import java.util.Arrays;
import java.util.stream.Collectors;

public class p11 {
    public static void main(String[] args) {
        String s1 = "Hello Midhun, Welcome to Kerala.";
        String oldWord = "Hello";
        String newWord = "Hi";

        String replacedString = Arrays.stream(s1.split(" ")).map(word -> word.equals(oldWord) ? newWord : word).collect(Collectors.joining(" "));
        System.out.println(replacedString);
    }
}
