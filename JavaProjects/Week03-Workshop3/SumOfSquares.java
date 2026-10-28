/*
 * BIT235 Workshop 3 - Part 3, Exercise 4A
 * Compute the sum of the squares of the first 100 integers.
 * 1^2 + 2^2 + ... + 100^2 = 338350
 */
public class SumOfSquares {
    public static void main(String[] args) {
        int sum = 0;

        for (int number = 1; number <= 100; number++) {
            sum = sum + (number * number);
        }

        System.out.println("Sum of the squares of the first 100 integers:");
        System.out.println("1^2 + 2^2 + ... + 100^2 = " + sum);
    }
}
