import java.io.*;
import java.util.*;

public class day22 {

    public static void main(String[] args) throws IOException {
        String pathname = "/Users/gaoyuan/Developer/Java/day2.txt";
        File filename = new File(pathname);
        InputStreamReader reader = new InputStreamReader(new FileInputStream(filename));
        BufferedReader br = new BufferedReader(reader);
        String line;

        List<String> input = new ArrayList<>();
        while ((line = br.readLine()) != null) {
            input.add(line);
        }
        String same;
        String outPut = "";
        int count;
        int min = 0;
        for (int i = 0; i < input.size() - 1; i++) {
            for (int j = i + 1; j < input.size(); j++) {
                count = 0;
                same = "";
                for (int k = 0; k < input.get(i).length(); k++) {
                    if (input.get(i).charAt(k) == input.get(j).charAt(k)) {
                        count++;
                        same += input.get(i).charAt(k);
                    }
                }
                if (count >= min) {
                    min = count;
                    outPut = same;
                }
            }
        }
        System.out.println(outPut);
    }
}


