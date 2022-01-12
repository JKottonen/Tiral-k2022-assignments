public class Lucky {
    public boolean check(int n) {
        String parsedNumber = String.valueOf(n);
        int sum = 0;
        for (int i = 0; i < parsedNumber.length(); i++) {
            sum += Integer.parseInt(Character.toString(parsedNumber.charAt(i)));
        }
        if (sum % 7 == 0) {
            return true;
        }
        else {
            return false;
        }

    }

    public static void main(String[] args) {
        Lucky l = new Lucky();
        System.out.println(l.check(14)); // false
        System.out.println(l.check(16)); // true
        System.out.println(l.check(123)); // false
        System.out.println(l.check(777)); // true
        System.out.println(l.check(9999999)); // true
    }
}