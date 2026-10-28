import java.util.Scanner;

/*
 * BIT235 Workshop 3 - Part 3, Exercise 3
 * Read an integer between 0 and 35 and display it in "base 36":
 * 0..9 stay digits, 10..35 become A..Z.
 */
public class NumberToLetter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter an integer between 0 and 35:");
        int number = scanner.nextInt();

        if (number < 0 || number > 35) {
            System.out.println("Invalid input: the number must be between 0 and 35.");
        } else if (number <= 9) {
            System.out.println("Result: " + number);
        } else {
            // A = 65, so 10 -> 'A' (65), 11 -> 'B' (66) ... 35 -> 'Z' (90)
            char letter = (char) (number + 55);
            System.out.println("Result: " + letter);
        }

        scanner.close();
    }
}
