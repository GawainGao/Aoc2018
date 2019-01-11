import java.io.*;
import java.util.*;

public class day42 {

    public static void main(String[] args) throws IOException {
        String pathname = "/Users/gaoyuan/Developer/Java/day4.txt";
        File filename = new File(pathname);
        InputStreamReader reader = new InputStreamReader(new FileInputStream(filename));
        BufferedReader br = new BufferedReader(reader);
        String line;
        List<String> input = new ArrayList<>();
        while ((line = br.readLine()) != null){
            input.add(line);
        }
        Collections.sort(input);
        int guard = 0;
        List<Integer> guardList = new ArrayList<>();
        int time;
        int[] guardTime = new int[10000];
        for  (int num = 0; num < input.size(); num ++) {
            String[] left = input.get(num).split("]");
            String[] date = left[0].split(" ");
            String[] ymd = date[0].split("-");
            String[] hm = date[1].split(":");
            //int year = Integer.parseInt(ymd[0]);
            int month = Integer.parseInt(ymd[1]);
            int day = Integer.parseInt(ymd[2]);
            int hour = Integer.parseInt(hm[0]);
            int min = Integer.parseInt(hm[1]);
            int dayday = day + month * 31;
            String[] right = left[1].split(" ");
            if (hour == 23) {
                hour = 0;
                min = 0;
            }
            if (right[1].charAt(0) == 'G') {
                guard = Integer.parseInt(right[2].substring(1));
                if (!guardList.contains(guard)){
                    guardList.add(guard);
                }
            }
        }
        int maxPeople = 0;
        int total_max = 0;
        int total_max_time = 0;
        for (Integer e : guardList){
            int[] timeTable = new int[60];
            for  (int num = 0; num < input.size(); num ++) {
                String[] left = input.get(num).split("]");
                String[] date = left[0].split(" ");
                String[] ymd = date[0].split("-");
                String[] hm = date[1].split(":");
                //int year = Integer.parseInt(ymd[0]);
                int month = Integer.parseInt(ymd[1]);
                int day = Integer.parseInt(ymd[2]);
                int hour = Integer.parseInt(hm[0]);
                int min = Integer.parseInt(hm[1]);
                int dayday = day + month * 31;
                String[] right = left[1].split(" ");
                if (hour == 23) {
                    hour = 0;
                    min = 0;
                }
                if (right[1].charAt(0) == 'G') {
                    guard = Integer.parseInt(right[2].substring(1));
                    time = 60 - 60;
                }
                if (guard == e){
                    if (right[1].charAt(0) == 'f'){
                        for (int k = min; k < 60; k++){
                            timeTable[k] += 1;
                        }
                    } else if (right[1].charAt(0) == 'w') {
                        for (int k = min; k < 60; k++){
                            timeTable[k] -= 1;
                        }
                    }
                }
            }
            int max = 0;
            int max_time = 0;
            for (int k = 0; k < 60; k++){
                if (timeTable[k] > max){
                    max = timeTable[k];
                    max_time = k;
                }
            }
            if (max > total_max){
                total_max = max;
                total_max_time = max_time;
                maxPeople = e;
            }
        }
        System.out.println(maxPeople * total_max_time);
    }
}


