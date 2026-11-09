/**
 * Workshop - Method Overloading, Part 4: Validating Overloaded Methods.
 *
 * The Printer class from the sheet, plus the extra overload print(double).
 * Class Main from the sheet becomes PrinterDemo so that it matches the file name.
 */
public class PrinterDemo {

    public static void main(String[] args) {
        Printer printer = new Printer();
        printer.print("Hello");        // print(String)
        printer.print(42);             // print(int)
        printer.print("Hello", 42);    // print(String, int)
        printer.print(3.14);           // print(double) - the new overload
    }
}

class Printer {

    void print(String message) {
        System.out.println("Message: " + message);
    }

    void print(int number) {
        System.out.println("Number: " + number);
    }

    void print(String message, int number) {
        System.out.println("Message and Number: " + message + ", " + number);
    }

    // Added for Part 4: a different parameter type, so this is a legal overload.
    void print(double value) {
        System.out.println("Double value: " + value);
    }
}
