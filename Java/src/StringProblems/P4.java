// Replace All Occurrences of a String

package StringProblems;

public class P4 {
    public static void main(String[] args) {
        String str = "Welcome GeeksforGeeks, Welcome geeks";
        String wordToReplace = "Welcome";
        String replacementWord = "Hello";
        String result = str.replaceAll("(?i)"+wordToReplace, replacementWord);
        System.out.println(result);
    }
}
