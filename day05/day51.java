import java.io.*;
import java.util.*;

public class day51 {

    public static void main(String[] args) throws Exception {
        File file = new File("/Users/gaoyuan/Developer/Java/day5.txt");
        Scanner input = new Scanner(file);
        String in = input.next();
        boolean flag = true;
        while (flag){
            for (int i=0; i<in.length()-1; i++){
                flag = false;
                if ((int)in.charAt(i) - (int)in.charAt(i + 1) == 'a' - 'A' || (int)in.charAt(i) - (int)in.charAt(i + 1) == 'A' - 'a') { //97-65 = 28 > 25
                    in = in.substring(0,i) + in.substring(i+2);
                    flag = true;
                    break;
                }
            }
        }
        System.out.println(in.length());
    }
}


