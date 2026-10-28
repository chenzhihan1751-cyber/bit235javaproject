/*
 * BIT235 Workshop 3 - Part 2
 * Converting a String to a primitive with Integer.parseInt().
 */
public class AgeStringToInt {
    public static void main(String[] args) {
        String ageText = "21";

        int age = Integer.parseInt(ageText);

        System.out.println("Age stored as a String : " + ageText);
        System.out.println("Age converted to an int: " + age);
        System.out.println("Proof it is a number   : " + age + " + 1 = " + (age + 1));
    }
}
