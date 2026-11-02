/*
 * BIT235 Object Oriented Programming - Week 4
 * Methods exercise, Question 4: returning method with two parameters.
 */
public class RandomNumber {

    public static void main(String[] args) {
        int small = randomNumber(5, 7);
        System.out.println("Random number between 5 and 7: " + small);

        System.out.println("Your random number: " + randomNumber(1, 100));
        System.out.println("A dice roll: " + randomNumber(1, 6));
    }

    // Returns a random whole number between low and high, both inclusive.
    // The range size is (high - low + 1) because both ends count.
    public static int randomNumber(int low, int high) {
        return (int) (Math.random() * (high - low + 1)) + low;
    }
}
