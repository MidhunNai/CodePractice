//Program to check if string contain any whitespace charecters

package StringProblems;

public class P2 {
    public static void main(String[] args) {
        String str = "MynameisMidhunNair.";
        boolean isWhiteSpace = checkWhiteSpace(str);
        System.out.println("Does string have whitespaces: " + isWhiteSpace);
    }

    public static boolean checkWhiteSpace(String str){
        if(str == null || str.isEmpty()){
            return false;
        }
        boolean isWhiteSpace = str.matches(".*\\s.*");
        return isWhiteSpace;
    }


}
