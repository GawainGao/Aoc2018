import java.io.*;
import java.util.*;

public class day31 {

    public static void main(String[] args) throws IOException {
        String pathname = "/Users/gaoyuan/Developer/Java/day3.txt";
        File filename = new File(pathname);
        InputStreamReader reader = new InputStreamReader(new FileInputStream(filename));
        BufferedReader br = new BufferedReader(reader);
        String line;

        boolean[][] totalMatrix = new boolean[1000][1000];
        boolean[][] flagMatrix = new boolean[1000][1000];
        List<String> input = new ArrayList<>();
        while ((line = br.readLine()) != null) {
            String[] left = line.split("@");
            String[] right = left[1].split(":");
            String[] xy = right[0].split(",");
            String[] widthHeight = right[1].split("x");
            int x = Integer.parseInt(xy[0].substring(1));
            int y = Integer.parseInt(xy[1]);
            int width = Integer.parseInt(widthHeight[0].substring(1));
            int height = Integer.parseInt(widthHeight[1]);
            for (int i = y; i < y + height; i++){
                for (int j = x; j < x +width; j++){
                    if(flagMatrix[i][j]){
                        totalMatrix[i][j]=true;
                    }
                    else{
                        flagMatrix[i][j]=true;
                    }
                }
            }
        }
        int total = 0;
        for (int i = 0; i < 1000; i++){
            for (int j = 0; j < 1000; j++){
                total += (totalMatrix[i][j]?1:0);
            }
        }
        System.out.println(total);
    }
}


