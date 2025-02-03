//Get a Number of Vowels in a String

package StringProblems;

public class p13 {
    public static void main(String[] args) {
        String s1 = "Hello Midhun, welcome to Kerala.";
        System.out.println(getVowelCount(s1));
    }

    public static int getVowelCount(String str) {
        int vowelCount = 0;
        for(char charecter : str.toCharArray()) {
            if(charecter == 'a' || charecter == 'e' || charecter == 'i' || charecter == 'o' || charecter == 'u'){
                vowelCount++;
            }
        }
        return vowelCount;
    }
}
