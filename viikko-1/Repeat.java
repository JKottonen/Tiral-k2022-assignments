public class Repeat {
    public int find(String s) {
        return 1;
    }

    public static void main(String[] args) {
        Repeat r = new Repeat();
        System.out.println(r.find("aaa")); // 1
        System.out.println(r.find("abcd")); // 4
        System.out.println(r.find("abcabcabcabc")); // 3
        System.out.println(r.find("aybabtuaybabtu")); // 7
        System.out.println(r.find("abcabca")); // 7
    }
}