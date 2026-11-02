/*
 * BIT235 Object Oriented Programming - Week 4
 * Arrays exercise, Q4: traversing an array with a foreach loop.
 */
public class ForEachTraversal {

    public static void main(String[] args) {
        int[] values = new int[5];
        values[0] = 12;
        values[1] = 4;
        values[2] = 1;
        values[3] = 8;
        values[4] = 7;

        // The foreach loop hands us each value; we never touch the index.
        for (int value : values) {
            System.out.println(value);
        }
    }
}
