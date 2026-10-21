import java.util.Scanner;

/**
 * BIT235 Workshop 2 - Exercise 1.8
 * Compare two strings that the user enters,
 * and also compare their first characters.
 */
public class Exercise1_8 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the first string : ");
        String firstString = input.nextLine();

        System.out.print("Enter the second string: ");
        String secondString = input.nextLine();

        boolean sameText = firstString.equals(secondString);
        System.out.println("Are the two given strings equal? " + sameText);

        char firstChar = firstString.charAt(0);
        char secondChar = secondString.charAt(0);
        boolean sameFirstCharacter = firstChar == secondChar;

        System.out.println("First character of string 1 : " + firstChar);
        System.out.println("First character of string 2 : " + secondChar);
        System.out.println("Are the first characters equal? "
                           + sameFirstCharacter);

        input.close();
    }
}