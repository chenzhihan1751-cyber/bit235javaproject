/*
 * BIT235 Object Oriented Programming - Week 4
 * Methods exercise, Question 2: void method with one int parameter.
 */
public class DisplayNumber {

    public static void main(String[] args) {
        displayNumber(7);
        displayNumber(42);
    }

    // void = returns nothing, but it accepts one int value from the caller.
    public static void displayNumber(int number) {
        System.out.println("The number is: " + number);
    }
}
