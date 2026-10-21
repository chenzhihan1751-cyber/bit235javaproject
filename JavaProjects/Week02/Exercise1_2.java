import java.util.Scanner;

/**
 * BIT235 Workshop 2 - Exercise 1.2
 * Convert degrees Celsius to degrees Fahrenheit.
 * Formula: F = C * 9 / 5 + 32  (9.0 / 5 keeps the division a double)
 */
public class Exercise1_2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the temperature in Celsius: ");
        double celsius = input.nextDouble();

        double fahrenheit = celsius * 9.0 / 5 + 32;

        System.out.println(celsius + " degrees Celsius = " + fahrenheit
                           + " degrees Fahrenheit");

        input.close();
    }
}