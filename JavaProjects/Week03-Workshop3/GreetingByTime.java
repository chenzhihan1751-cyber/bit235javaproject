import java.util.Scanner;

/*
 * BIT235 Workshop 3 - Part 3, Exercise 1 (a)
 * Read an hour between 1 and 24 and print the matching greeting.
 */
public class GreetingByTime {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter a number between 1 and 24:");
        int hour = scanner.nextInt();

        if (hour < 1 || hour > 24) {
            System.out.println("Invalid input: the number must be between 1 and 24.");
        } else if (hour < 18) {
            System.out.println("Good day");
        } else {
            System.out.println("Good evening");
        }

        scanner.close();
    }
}
