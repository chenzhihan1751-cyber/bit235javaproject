/*
 * BIT235 Workshop 3 - Part 2
 * Converting a primitive to a String with String.valueOf().
 *
 * A boolean "status" flag is converted to text before it is written to a
 * database / displayed on a web page.
 */
public class BooleanToString {
    public static void main(String[] args) {
        boolean status = true;

        String statusText = String.valueOf(status);

        System.out.println("boolean status                : " + status);
        System.out.println("String.valueOf(status)        : " + statusText);
        System.out.println("Characters in the String      : " + statusText.length());

        boolean inactive = false;
        String inactiveText = String.valueOf(inactive);

        System.out.println();
        System.out.println("boolean inactive status       : " + inactive);
        System.out.println("String.valueOf(inactive)      : " + inactiveText);
    }
}
