import java.util.Scanner;

/*
 * BIT235 Workshop 3 - Part 3, Exercise 2
 * Read three numbers and display the smallest number(s) - all of them
 * when two or three values are equal.
 */
public class SmallestOfThree {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter the first number:");
        double first = scanner.nextDouble();
        System.out.println("Enter the second number:");
        double second = scanner.nextDouble();
        System.out.println("Enter the third number:");
        double third = scanner.nextDouble();

        double smallest = first;
        if (second < smallest) {
            smallest = second;
        }
        if (third < smallest) {
            smallest = third;
        }

        System.out.println();
        System.out.println("The numbers are : " + first + ", " + second
                + ", " + third);
        System.out.print("The smallest number(s): ");

        if (first == smallest) {
            System.out.print(first + " ");
        }
        if (second == smallest) {
            System.out.print(second + " ");
        }
        if (third == smallest) {
            System.out.print(third + " ");
        }
        System.out.println();

        scanner.close();
    }
}
