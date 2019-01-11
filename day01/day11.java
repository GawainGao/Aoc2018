import java.io.*;

public class day11 {

    public static void main(String[] args) throws IOException
    {
        String pathname = "/Users/gaoyuan/Developer/Java/day1-2.txt";
        File filename = new File(pathname);
        InputStreamReader reader = new InputStreamReader(new FileInputStream(filename));
        BufferedReader br = new BufferedReader(reader);
        String line;
        int totalPlus = 0;
        int totalMinus = 0;
        while ((line = br.readLine())!= null){
            if ("+".equals(line.substring(0,1))) {
                totalPlus += Integer.parseInt(line.substring(1));
            } else{
                totalMinus += Integer.parseInt(line.substring(1));
            }
        }
        System.out.println(totalPlus - totalMinus);
    }
}

