/**
 * BIT235 Workshop 2 - Exercise 1.7
 * "I love java programming".substring(7, 11) -> length and content of the string
 */
public class Exercise1_7 {
    public static void main(String[] args) {
        String text = "I love java programming";
        String result = text.substring(7, 11);

        System.out.println("Original string : " + text);
        System.out.println("substring(7, 11): \"" + result + "\"");
        System.out.println("Length          : " + result.length());
    }
}