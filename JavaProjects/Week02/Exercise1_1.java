import java.util.Scanner;

/**
 * BIT235 Workshop 2 - Exercise 1.1
 * Display the difference of two integers entered by the user.
 */
public class Exercise1_1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the first integer : ");
        int firstNumber = input.nextInt();

        System.out.print("Enter the second integer: ");
        int secondNumber = input.nextInt();

        int difference = firstNumber - secondNumber;

        System.out.println("First number  = " + firstNumber);
        System.out.println("Second number = " + secondNumber);
        System.out.println("Difference    = " + firstNumber + " - "
                           + secondNumber + " = " + difference);

        input.close();
    }
}