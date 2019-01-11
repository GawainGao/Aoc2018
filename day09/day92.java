import java.util.*;

public class day92 {

    public static void main(String[] args){
        int num = 427;
        int marble = 70723;
        LinkedList<Integer> deque = new LinkedList<>();
        int[] point = new int[num];
        int p = 0;
        for (int i = 0; i<marble+1; i++){
            if (i % 23 == 0 && i > 0){
                p = i % num;
                Collections.rotate(deque,-6);
                point[p] += (i + deque.pop());
                //System.out.println(i);
            }
            else {
                Collections.rotate(deque,2);
                deque.add(i);
            }
            //System.out.println(deque);
        }
        int maxm = 0;
        for (int i : point){
            maxm = (i > maxm)?i:maxm;
        }
        System.out.println(maxm);
    }
}
