import java.io.*;
import java.util.*;

public class day32 {

    public static void main(String[] args) throws IOException {
        String pathname = "/Users/gaoyuan/Developer/Java/day3.txt";
        File filename = new File(pathname);
        InputStreamReader reader = new InputStreamReader(new FileInputStream(filename));
        BufferedReader br = new BufferedReader(reader);
        String line;

        int[][] totalMatrix = new int[1000][1000];
        boolean flag;
        List<String> input = new ArrayList<>();
        while ((line = br.readLine()) != null){
            input.add(line);
        }

        for  (int num = 0; num < input.size(); num ++){
            String[] left = input.get(num).split("@");
            String[] right = left[1].split(":");
            String[] xy = right[0].split(",");
            String[] widthHeight = right[1].split("x");
            int x = Integer.parseInt(xy[0].substring(1));
            int y = Integer.parseInt(xy[1]);
            int width = Integer.parseInt(widthHeight[0].substring(1));
            int height = Integer.parseInt(widthHeight[1]);

            for (int i = y; i < y + height; i++){
                for (int j = x; j < x +width; j++){
                    totalMatrix[i][j]++;
                }
            }
        }
        for  (int num = 0; num < input.size(); num ++){
            String[] left = input.get(num).split("@");
            String[] right = left[1].split(":");
            String[] xy = right[0].split(",");
            String[] widthHeight = right[1].split("x");
            int x = Integer.parseInt(xy[0].substring(1));
            int y = Integer.parseInt(xy[1]);
            int width = Integer.parseInt(widthHeight[0].substring(1));
            int height = Integer.parseInt(widthHeight[1]);
            flag = true;
            for (int i = y; i < y + height; i++){
                for (int j = x; j < x +width; j++){
                    flag = flag && (totalMatrix[i][j] == 1);
                }
            }
            if (flag == true){
                System.out.println(num + 1);
                break;
            }
        }
    }
}


