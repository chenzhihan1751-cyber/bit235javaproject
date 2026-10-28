/*
 * BIT235 Workshop 3 - Part 1
 * Using StringBuffer for Dynamic User Messages
 *
 * The three ellipses of the original skeleton are replaced by the three
 * lines marked with "ANSWER" below.
 */
public class WelcomeMessage {
    public static void main(String[] args) {
        String name = "Alice";
        String city = "Melbourne";

        // Use StringBuffer to construct a personalized message
        StringBuffer message = new StringBuffer("Welcome, ");      // ANSWER 1
        message.append(name).append("! We hope you're enjoying "); // ANSWER 2
        message.append("your time in ").append(city).append(".");  // ANSWER 3

        System.out.println(message);

    }
}
