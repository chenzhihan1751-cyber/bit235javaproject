public class Exercise2 {
    public static void main(String[] args) {
        int a = 12;
        int b = 5;

        System.out.println("a + b = " + (a + b));
        System.out.println("a - b = " + (a - b));
        System.out.println("a * b = " + (a * b));
        System.out.println("a / b = " + (a / b));
        System.out.println("a % b = " + (a % b));

        System.out.println();
        System.out.println("a and b are both int, so a / b is integer division.");
        System.out.println("12 / 5 is really 2.4, but the .4 is dropped, so it prints 2.");
        System.out.println("a % b is the remainder: 5 * 2 = 10, and 12 - 10 = 2.");
    }
}
