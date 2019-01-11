import java.io.*;
import java.util.*;
import java.util.List;

class Point {
    int x;
    int y;
    Point(String s){
        String[] left = s.split(",");
        x = Integer.parseInt(left[0]);
        y = Integer.parseInt(left[1].substring(1));
    }
}

public class day62 {

    public static void main(String[] args) throws Exception {
        File file = new File("day6.txt");
        Scanner input = new Scanner(file);
        List<String> inputList = new ArrayList<>();
        while (input.hasNextLine()){
            inputList.add(input.nextLine());
        }
        int distance;
        int count = 0;
        int[][] res2 = new int[500][500];
        for (int i = 0; i < 500; i ++){
            for (int j = 0; j < 500; j++){
                for (String in: inputList) {
                    Point point = new Point(in);
                    distance = Math.abs(point.x - i) + Math.abs(point.y - j);
                    res2[i][j] += distance;
                }
                if (res2[i][j] < 10000){
                    count++;
                }
            }
        }
        System.out.println(count);
    }
}


