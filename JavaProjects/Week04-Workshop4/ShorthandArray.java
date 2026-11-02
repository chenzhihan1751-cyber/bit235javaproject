import java.util.Arrays;

/*
 * BIT235 Object Oriented Programming - Week 4
 * Arrays exercise, Q1: creating an array with the shorthand method.
 */
public class ShorthandArray {

    public static void main(String[] args) {
        // Shorthand: the size is worked out from the number of values.
        int[] numbers = {3, 6, 9, 12, 15};

        System.out.println("numbers.length = " + numbers.length);
        System.out.println("numbers = " + Arrays.toString(numbers));
    }
}
