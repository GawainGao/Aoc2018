import java.util.*;

public class day91 {

    public static void main(String[] args){
        int num = 427;
        int[] player = new int[num];
        LinkedList<Integer> marble = new LinkedList<>();
        marble.add(0);
        marble.add(1);
        int position = 1;
        for (int i = 2; i < 70724; i++){
            int size = marble.size();
            if (i % 23 == 0) {
                System.out.println(i);
                if (position >= 9){
                    player[i%num] += (i + marble.get(position-9));
                    marble.remove(position-9);
                    position -=7;
                }
                else if (position - 7 >= -1){
                    player[i%num] += (i + marble.get(size-9+position));
                    marble.remove(size - 9 + position);
                    position -=6;
                }
                else {
                    player[i%num] += (i + marble.get(size-9+position));
                    marble.remove(size - 9 + position);
                    size = marble.size();
                    position = size + position - 7 + 1;
                }
            }
            else {
                if (size >= position){
                    marble.add(position,i);
                    position += 2;
                }
                else {
                    marble.add(1,i);
                    position = 3;
                }
            }
        }
        int maxm = 0;
        for (int i : player){
            maxm = (i > maxm)?i:maxm;
        }
        System.out.println(marble);
        System.out.println(maxm);
    }
}











