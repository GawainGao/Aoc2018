import java.io.*;
import java.util.*;

public class day21 {

    public static void main(String[] args) throws IOException
    {
        String pathname = "/Users/gaoyuan/Developer/Java/day2.txt";
        File filename = new File(pathname);
        InputStreamReader reader = new InputStreamReader(new FileInputStream(filename));
        BufferedReader br = new BufferedReader(reader);
        String line;
        int countNumber_2 = 0;
        int countNumber_3 = 0;
        while ((line = br.readLine())!= null){
            char[] elements = line.toCharArray();
            HashMap<Character,Integer> countNumber = new HashMap<>();
            for (char e:elements){
                if(!countNumber.containsKey(e)){
                    countNumber.put(e,1);
                }
                else{
                    countNumber.put(e,countNumber.get(e)+1);
                }
            }
            for (Integer value: countNumber.values()) {
                if (value == 2) {
                    countNumber_2++;
                    break;
                }
            }
            for (Integer value: countNumber.values()) {
                if (value == 3) {
                    countNumber_3++;
                    break;
                }
            }
        }
        System.out.println(countNumber_2 * countNumber_3);
    }
}

