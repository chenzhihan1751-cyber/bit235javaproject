/*
 * BIT235 Object Oriented Programming - Week 4
 * Arrays extended exercise, Exercise 1: passing an array to a method.
 */
public class CalculateTotal {

    public static void main(String[] args) {
        int[] values = {4, 7, 2, 9, 5};

        // The whole array (actually the reference to it) is passed in.
        int total = calculateTotal(values);

        System.out.println("Total: " + total);
    }

    // Static, takes one int array, returns an int.
    public static int calculateTotal(int[] numbers) {
        int total = 0;
        for (int value : numbers) {
            total = total + value;
        }
        return total;
    }
}
