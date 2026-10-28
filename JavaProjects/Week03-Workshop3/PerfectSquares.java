/*
 * BIT235 Workshop 3 - Part 3, Exercise 4B
 * Display all the integers between 1 and 100 that are perfect squares.
 * A number is a perfect square when its square root is a whole number.
 */
public class PerfectSquares {
    public static void main(String[] args) {
        System.out.println("Perfect squares between 1 and 100:");

        for (int number = 1; number <= 100; number++) {
            int root = (int) Math.sqrt(number);
            if (root * root == number) {
                System.out.println(number + " = " + root + " x " + root);
            }
        }
    }
}
