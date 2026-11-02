import java.util.Scanner;

/*
 * BIT235 Object Oriented Programming - Week 4
 * Arrays exercise, Q7: filling an array at runtime and printing it.
 *
 * Note: a foreach loop cannot fill an array. It copies each element into a
 * local variable, so writing to that variable never reaches the array. That
 * is why a normal for loop with an index is used to read the input, and the
 * foreach loop is used to display the finished array.
 */
public class FillArrayAtRuntime {

    public static void main(String[] args) {
        String[] people = new String[5];
        Scanner scanner = new Scanner(System.in);
        int count = 0;

        System.out.println("Enter up to 5 names (empty line to stop):");
        for (int i = 0; i < people.length; i++) {
            String input = scanner.nextLine().trim();
            if (input.isEmpty()) {
                break;              // user entered nothing, stop asking
            }
            people[i] = input;
            count++;
        }
        scanner.close();

        System.out.println("Number of names entered: " + count);
        System.out.print("People: ");
        boolean first = true;
        for (int i = 0; i < count; i++) {
            if (!first) {
                System.out.print(", ");
            }
            System.out.print(people[i]);
            first = false;
        }
        System.out.println();
    }
}
