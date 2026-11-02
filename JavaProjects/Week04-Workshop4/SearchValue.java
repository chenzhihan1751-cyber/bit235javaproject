/*
 * BIT235 Object Oriented Programming - Week 4
 * Arrays exercise, Q5: searching for a value with a loop and an if statement.
 */
public class SearchValue {

    public static void main(String[] args) {
        int[] numbers = {3, 6, 9, 12, 15};
        int target = 9;
        boolean found = false;

        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] == target) {
                found = true;
                break;          // no need to keep looking once it is found
            }
        }

        if (found) {
            System.out.println("Value found");
        } else {
            System.out.println("Value not found");
        }
    }
}
