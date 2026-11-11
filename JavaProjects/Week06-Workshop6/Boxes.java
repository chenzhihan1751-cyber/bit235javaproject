/*
 * BIT235 Workshop 6 - Exercise 7 (Medium) - part 1 of 2
 *
 * Boxes: a class that draws a square box on the console.
 *
 *   '-'  top and bottom line
 *   '|'  left and right side
 *   the box is a square, so size 5 means 5 columns and 5 rows
 *
 * The class provides everything the question asks for:
 *   - a constructor that accepts the size of the box
 *   - setSize(int) to change the size later
 *   - toString() that returns the size as a String, e.g. "10 x 10"
 *   - draw() that prints the box
 *
 * A size below 1 or above MAX_SIZE (10) is refused and the old size is
 * kept, so the box can never be drawn larger than 10 x 10.
 */
public class Boxes {

    public static final int MIN_SIZE = 1;
    public static final int MAX_SIZE = 10;

    private int size;

    /** Constructor: accepts the size of the box (1..10). */
    public Boxes(int size) {
        this.size = 1;          // safe default before validation
        setSize(size);
    }

    /** Sets the size of the box; returns true when the size was accepted. */
    public boolean setSize(int size) {
        if (size < MIN_SIZE || size > MAX_SIZE) {
            System.out.println("  [Boxes] size " + size + " is outside "
                    + MIN_SIZE + ".." + MAX_SIZE + ", keeping " + this.size);
            return false;
        }
        this.size = size;
        return true;
    }

    public int getSize() {
        return size;
    }

    /** Returns the size of the box as a String, for example "10 x 10". */
    public String toString() {
        return size + " x " + size;
    }

    /** Draws the box on the console. */
    public void draw() {
        drawLine();                             // top
        for (int row = 0; row < size - 2; row++) {
            System.out.print('|');
            for (int col = 0; col < size - 2; col++) {
                System.out.print(' ');
            }
            System.out.println('|');
        }
        if (size > 1) {
            drawLine();                         // bottom
        }
    }

    /** Helper: one horizontal border of 'size' hyphens. */
    private void drawLine() {
        for (int col = 0; col < size; col++) {
            System.out.print('-');
        }
        System.out.println();
    }
}
