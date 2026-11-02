/*
 * BIT235 Object Oriented Programming - Week 4
 * Arrays exercise, Q3: traversing an array with a for loop and .length.
 */
public class ForLoopTraversal {

    public static void main(String[] args) {
        int[] numbers = {3, 6, 9, 12, 15};

        // i runs from 0 to numbers.length - 1, so no index is skipped or missed.
        for (int i = 0; i < numbers.length; i++) {
            System.out.println(numbers[i]);
        }
    }
}
