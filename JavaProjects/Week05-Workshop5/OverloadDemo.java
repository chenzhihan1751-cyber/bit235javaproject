/**
 * Workshop - Method Overloading, Part 1: Predicting Method Overloading Behavior.
 *
 * The code below is the code given in the workshop sheet, unchanged. Running it
 * shows which overload the compiler picks for each call in main().
 */
public class OverloadDemo {

    public static void display(int num) {
        System.out.println("Integer: " + num);
    }

    public static void display(double num) {
        System.out.println("Double: " + num);
    }

    public static void display(String str) {
        System.out.println("String: " + str);
    }

    public static void main(String[] args) {
        display(5);        // exact match: display(int)
        display(5.5);      // exact match: display(double)
        display("Hello");  // exact match: display(String)
        display('A');      // char -> widening to int => display(int), prints 65
        display(100L);     // long -> widening to double => display(double)
    }
}
