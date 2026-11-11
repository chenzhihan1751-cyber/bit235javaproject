/*
 * BIT235 Workshop 6 - Exercise 6 (Easy) - part 2 of 2
 *
 * Runs the code from the question and prints its real output, so the
 * written answer can be checked against a live run.
 *
 * Expected reasoning:
 *   a.y = 5   -> a has its own instance variable y
 *   b.y = 6   -> b has its own instance variable y
 *   a.x = 2   -> a.x = 1 and then b.x = 2 both write the SAME static
 *                field, so the last write wins
 *   b.x = 2
 *   IdentifyMyParts.x = 2
 */
public class IdentifyPartsDemo {

    public static void main(String[] args) {

        System.out.println("Class variables (static)   : x");
        System.out.println("Instance variables         : y");
        System.out.println();

        IdentifyMyParts a = new IdentifyMyParts();
        IdentifyMyParts b = new IdentifyMyParts();

        a.y = 5;
        b.y = 6;
        a.x = 1;
        b.x = 2;

        System.out.println("a.y = " + a.y);
        System.out.println("b.y = " + b.y);
        System.out.println("a.x = " + a.x);
        System.out.println("b.x = " + b.x);
        System.out.println("IdentifyMyParts.x = " + IdentifyMyParts.x);
    }
}
