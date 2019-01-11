import java.io.*;
import java.util.*;
import java.util.List;

class Point{
    int x;
    int y;
    Point(String s){
        String[] left = s.split(",");
        x = Integer.parseInt(left[0]);
        y = Integer.parseInt(left[1].substring(1));
    }
}

public class day61 {

    public static void main(String[] args) throws Exception {
        File file = new File("day6.txt");
        Scanner input = new Scanner(file);
        List<String> inputList = new ArrayList<>();
        while (input.hasNextLine()){
            inputList.add(input.nextLine());
        }
        int distance;
        int mini;
        int[][] res = new int[500][500];
        List<Integer> edge = new ArrayList<>();
        Map<Integer,Integer> map = new HashMap<>();
        for (int i = 0; i < 500; i ++){
            for (int j = 0; j < 500; j++){
                mini = 1000;
                for (String in: inputList) {
                    Point point = new Point(in);
                    distance = Math.abs(point.x - i) + Math.abs(point.y - j);
                    if (distance == mini) {
                        res[i][j] = 1000;
                    }
                    else if (distance < mini){
                        mini = distance;
                        res[i][j] = inputList.indexOf(in);
                    }

                }
                Integer num = map.get(res[i][j]);
                map.put(res[i][j],num == null? 1 : num + 1);
                if (i ==0 || i == 499 || j == 0 || j == 499){
                    edge.add(res[i][j]);
                }
            }
        }
        int maxm = 0;
        Iterator it = map.keySet().iterator();
        while (it.hasNext()){
            Object key = it.next();
            if (maxm < map.get(key) && !edge.contains(key)){
                maxm = map.get(key);
            }
        }
        System.out.println(maxm);
    }
}


