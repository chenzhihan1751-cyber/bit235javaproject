/*
 * BIT235 Workshop 6 - Exercise 7 (Medium) - part 2 of 2
 *
 * Driver class: contains main() and makes the calls to the Boxes class,
 * so the Boxes class itself has no main() of its own.
 *
 * Two box sizes are drawn (5 x 5 and 3 x 3) exactly like the example in
 * the question. toString(), the maximum size and setSize() are then
 * checked so every requirement of the class is exercised.
 */
public class BoxesDriver {

    public static void main(String[] args) {

        System.out.println("Test 1: new Boxes(5)");
        Boxes box5 = new Boxes(5);
        System.out.println("  toString() -> " + box5);
        box5.draw();

        System.out.println();
        System.out.println("Test 2: new Boxes(3)");
        Boxes box3 = new Boxes(3);
        System.out.println("  toString() -> " + box3);
        box3.draw();

        System.out.println();
        System.out.println("Test 3: maximum size, new Boxes(10) -> " + new Boxes(10));

        System.out.println();
        System.out.println("Test 4: box5.setSize(7)");
        System.out.println("  before -> " + box5);
        box5.setSize(7);
        System.out.println("  after  -> " + box5);

        System.out.println();
        System.out.println("Test 5: box5.setSize(15) is out of range");
        box5.setSize(15);
        System.out.println("  size is still " + box5);
    }
}
