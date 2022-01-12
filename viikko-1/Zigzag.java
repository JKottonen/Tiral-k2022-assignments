import java.util.*;

public class Zigzag {
    public int[] create(int n) {
        int[] zigzaglist = new int[n];
        int center = Math.floorDiv(n, 2);
        int offset = 0;
        boolean rightSide = false;

        for (int i = 0; i < n; i++) {
            if(rightSide) {
                zigzaglist[center + offset] = i + 1;
                rightSide = !rightSide;
            }
            else {
                zigzaglist[center - offset] = i + 1;
                rightSide = !rightSide;
                offset ++;
            }
        }

        return zigzaglist;
    }

    public static void main(String[] args) {
        Zigzag z = new Zigzag();
        System.out.println(Arrays.toString(z.create(1))); // [1]
//        System.out.println(Arrays.toString(z.create(2))); // [1,2]
        System.out.println(Arrays.toString(z.create(3))); // [3,1,2]
  //      System.out.println(Arrays.toString(z.create(4))); // [3,1,2,4]
        System.out.println(Arrays.toString(z.create(5))); // [5,3,1,2,4]
    }
}