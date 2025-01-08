// Compare two strings

package StringProblems;

public class p10 {
    public static void main(String[] args) {
        String s1 = "My name is Midhun Nair";
        String s2 = "Midhun Nair";
        int ans = s1.compareTo(s2);
        String res;
        if(ans < 0){
            res = s1 + " comes befor " + s2;
        } else if(ans == 0){
            res = "both strings are same";
        } else {
            res = s1 + " comes afrer " + s2;
        }
        System.out.println(res);
    }
}
