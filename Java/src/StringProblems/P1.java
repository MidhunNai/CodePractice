package StringProblems;

// Program to count words of a string

public class P1 {
    public static int countWords(String str){
        if(str == null || str.trim().isEmpty()){
            return 0;
        }
        String[] words = str.trim().split("\\s+");
        return words.length;
    }
    public static void main(String[] args) {
        String str = "My name is Mishun Nair.";  
        int wordCount = countWords(str);
        System.out.println("The number of words in given string is: " + wordCount);
    }
}
