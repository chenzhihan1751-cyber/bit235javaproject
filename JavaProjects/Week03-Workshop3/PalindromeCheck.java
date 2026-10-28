import java.util.Scanner;

/*
 * BIT235 Workshop 3 - Part 1
 * Reversing Strings: check whether a word is a palindrome.
 * The word is reversed with StringBuffer.reverse() and compared with the
 * original word, ignoring upper/lower case and surrounding spaces.
 */
public class PalindromeCheck {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a word: ");
        String word = scanner.nextLine().trim();

        StringBuffer buffer = new StringBuffer(word);
        String reversed = buffer.reverse().toString();

        System.out.println("Original word : " + word);
        System.out.println("Reversed word : " + reversed);

        if (word.length() == 0) {
            System.out.println("No word was entered.");
        } else if (word.equalsIgnoreCase(reversed)) {
            System.out.println("Result        : \"" + word + "\" is a palindrome.");
        } else {
            System.out.println("Result        : \"" + word + "\" is NOT a palindrome.");
        }

        scanner.close();
    }
}
