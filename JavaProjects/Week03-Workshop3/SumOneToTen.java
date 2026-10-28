/*
 * BIT235 Workshop 3 - Part 3, Exercise 1 (c)
 * A while loop that adds up the values 1 to 10 and prints the sum.
 */
public class SumOneToTen {
    public static void main(String[] args) {
        int number = 1;
        int sum = 0;

        while (number <= 10) {
            sum = sum + number;
            number++;
        }

        System.out.println("Sum of the values 1 to 10 = " + sum);
    }
}
