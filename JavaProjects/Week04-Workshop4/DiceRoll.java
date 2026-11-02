/*
 * BIT235 Object Oriented Programming - Week 4
 * Methods exercise, Question 3: returning method with no parameters.
 */
public class DiceRoll {

    public static void main(String[] args) {
        int first = diceRoll();
        int second = diceRoll();
        int total = first + second;

        System.out.println("Your rolls: " + first + " and " + second + ".");
        if (total == 7) {
            System.out.println(total + " is a winner!!");
        } else {
            System.out.println("Try again.");
        }
    }

    // Math.random() gives 0.0 - 0.999..., so * 6 + 1 gives 1 - 6.999,
    // and the (int) cast cuts it down to a whole number from 1 to 6.
    public static int diceRoll() {
        return (int) (Math.random() * 6) + 1;
    }
}
