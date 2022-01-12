import java.util.*;

public class Zigzag {
    public int[] create(int n) {
        int[] result = new int[n];
        int k = (n-1)/2;
        for (int i = 1; i <= n; i++) {
            if (i%2 == 0) {
                result[k+i/2] = i;
            } else {
                result[k-i/2] = i;
            }
        }
        return result;
    }


    public static void main(String[] args) {
        Zigzag z = new Zigzag();
        System.out.println(Arrays.toString(z.create(1))); // [1]
        System.out.println(Arrays.toString(z.create(2))); // [1,2]
        System.out.println(Arrays.toString(z.create(3))); // [3,1,2]
        System.out.println(Arrays.toString(z.create(4))); // [3,1,2,4]
        System.out.println(Arrays.toString(z.create(20))); // [5,3,1,2,4]
    }
}