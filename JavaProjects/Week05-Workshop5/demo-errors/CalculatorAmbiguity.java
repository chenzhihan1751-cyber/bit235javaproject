/**
 * Workshop - Method Overloading, Part 2: the exact code from the sheet.
 *
 * This file is deliberately NOT compiled with the rest of the project: it does
 * not compile. javac reports the two problems that Part 2 asks about.
 *
 *   javac --release 8 demo-errors/CalculatorAmbiguity.java
 */
public class CalculatorAmbiguity {

    public static void main(String[] args) {
        System.out.println(calculate(10, 20L));
        System.out.println(calculate(10L, 20));
        System.out.println(calculate(10, 20L));
        System.out.println(calculate(10.5, 20.5));
    }

    public static int calculate(int a, long b) {
        System.out.println("Method 1");
        return (int) (a + b);
    }

    public static long calculate(long a, int b) {
        System.out.println("Method 2");
        return a + b;
    }
}
