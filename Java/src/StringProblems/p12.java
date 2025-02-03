//Frequency of characters Appearance

package StringProblems;

public class p12 {

    public static int getFrequenct(String str, char charToFind) {
        int frequency = 0;
        for(char charecter: str.toCharArray()){
            if(charecter == charToFind){
                frequency++;
            }
        }
        return frequency;
    }
    public static void main(String[] args) {
        String s1 = "Hello Midhun, whelcome to Kerala";
        char ch = 'e';
        System.out.println(getFrequenct(s1, ch));
        }
}