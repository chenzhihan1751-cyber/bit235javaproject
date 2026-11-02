/*
 * BIT235 Object Oriented Programming - Week 4
 * Arrays exercise, Q6: printing an array in reverse order.
 */
public class ReverseTraversal {

    public static void main(String[] args) {
        int[] values = new int[5];
        values[0] = 12;
        values[1] = 4;
        values[2] = 1;
        values[3] = 8;
        values[4] = 7;

        // Start at the last index (length - 1) and walk backwards to 0.
        for (int i = values.length - 1; i >= 0; i--) {
            System.out.println(values[i]);
        }
    }
}
