/**
 * Workshop - Method Overloading, Part 3: Understanding Method Overloading.
 *
 * One class called Calculator holding three overloaded multiply() methods.
 * The sheet writes "public static void main()"; the JVM entry point needs a
 * String[] parameter, so main(String[] args) is used here (same method names
 * and signatures otherwise).
 */
public class Calculator {

    // Two integers.
    public static int multiply(int a, int b) {
        return a * b;
    }

    // Two doubles -> the double overload is chosen when either argument is double.
    public static double multiply(double a, double b) {
        return a * b;
    }

    // Three integers -> different parameter list, so it is a valid overload.
    public static int multiply(int a, int b, int c) {
        return a * b * c;
    }

    public static void main(String[] args) {
        System.out.println("Multiplication of two integers: " + multiply(5, 3));
        System.out.println("Multiplication of two doubles: " + multiply(4.5, 4.5));
        System.out.println("Multiplication of three integers: " + multiply(4, 5, 6));
    }
}
