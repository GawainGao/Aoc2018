import java.io.*;
import java.util.*;

public class day12 {

    public static void main(String[] args) throws IOException
    {
        String pathname = "/Users/gaoyuan/Developer/Java/day1-2.txt";
        File filename = new File(pathname);
        InputStreamReader reader = new InputStreamReader(new FileInputStream(filename));
        BufferedReader br = new BufferedReader(reader);
        String line;
        boolean countinueFlag = true;
        List<Integer> sumList = new ArrayList<>();
        br.mark((int)filename.length() + 1);
        int sum = 0;
        sumList.add(0);
        while (countinueFlag)
        {
            while ((line = br.readLine())!= null){
                if ("+".equals(line.substring(0,1))) {
                    sum += Integer.parseInt(line.substring(1));
                } else{
                    sum -= Integer.parseInt(line.substring(1));
                }
                if (sumList.contains(sum))
                {
                    System.out.println(sum);
                    countinueFlag = false;
                }
                else
                {
                    sumList.add(sum);
                    //System.out.println(1);
                }
            }
            br.reset();
        }
    }
}

