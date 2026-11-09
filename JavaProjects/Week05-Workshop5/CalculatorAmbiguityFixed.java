/**
 * Workshop - Method Overloading, Part 2 (the calls that do compile).
 *
 * The sheet's Calculator had only the two int/long methods. calculate(10,20) is
 * ambiguous and calculate(10.5,20.5) has no applicable method, so those two calls
 * are commented out here; the full sheet version is in
 * demo-errors/CalculatorAmbiguity.java, where javac prints the errors.
 */
public class CalculatorAmbiguityFixed {

    public static int calculate(int a, long b) {
        System.out.println("Method 1");
        return (int) (a + b);
    }

    public static long calculate(long a, int b) {
        System.out.println("Method 2");
        return a + b;
    }

    public static void main(String[] args) {
        // Exact match: (int, long) -> Method 1.
        System.out.println(calculate(10, 20L));

        // Exact match: (long, int) -> Method 2.
        System.out.println(calculate(10L, 20));

        // calculate(10, 20)       -> ambiguous: each method needs exactly one
        //                            widening conversion, so neither is more specific.
        // calculate(10.5, 20.5)   -> no applicable method: double -> long would be
        //                            a narrowing conversion, which Java never does
        //                            implicitly (a cast such as (long) 10.5 is needed).
    }
}
