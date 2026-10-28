/*
 * BIT235 Workshop 3 - Part 3, Exercise 1 (b)
 * A while loop that prints the multiples of 5 between 10 and 95.
 */
public class MultiplesOfFive {
    public static void main(String[] args) {
        int number = 10;

        System.out.println("Multiples of 5 between 10 and 95:");

        while (number <= 95) {
            System.out.print(number + " ");
            number = number + 5;
        }

        System.out.println();
    }
}
