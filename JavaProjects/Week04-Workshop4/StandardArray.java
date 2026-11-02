import java.util.Arrays;

/*
 * BIT235 Object Oriented Programming - Week 4
 * Arrays exercise, Q2: creating an array with the standard method.
 */
public class StandardArray {

    public static void main(String[] args) {
        // Standard method: the size is fixed first, then values are assigned.
        int[] values = new int[5];
        values[0] = 12;
        values[1] = 4;
        values[2] = 1;
        values[3] = 8;
        values[4] = 7;

        System.out.println("values.length = " + values.length);
        System.out.println("values = " + Arrays.toString(values));
    }
}
