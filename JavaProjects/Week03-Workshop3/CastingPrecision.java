import java.math.BigDecimal;

/*
 * BIT235 Workshop 3 - Part 2
 * Casting between double, float and int: precision loss.
 *
 * 1) PI to 10 decimal places in a double, then narrowed to a float.
 * 2) A dollar amount with cents (23.99) stored in a double.
 * 3) The same amount with zero cents (23.00).
 *
 * new BigDecimal(double) shows the exact binary value that the double
 * really holds, which is what makes the rounding visible.
 */
public class CastingPrecision {
    public static void main(String[] args) {
        // ---------- Task 1: PI accurate to 10 decimal places ----------
        double piDouble = 3.1415926535;
        float piFloat = (float) piDouble;

        System.out.println("Task 1 - PI (10 decimal places)");
        System.out.println("PI as a double : " + piDouble);
        System.out.println("PI as a float  : " + piFloat);
        System.out.println("Difference     : " + (piDouble - piFloat));
        System.out.println("The float keeps only about 7 significant digits,");
        System.out.println("so the last decimal places of PI are lost.");
        System.out.println();

        // ---------- Task 2: 23.99 (dollars and cents) ----------
        double withCents = 23.99;

        System.out.println("Task 2 - dollar amount with 2 cent values");
        System.out.println("Stored value   : " + withCents);
        System.out.println("Exact double   : " + new BigDecimal(withCents));
        System.out.println("23.99 cannot be stored exactly in binary, so the double");
        System.out.println("holds a value slightly below 23.99.  println only shows");
        System.out.println("the shortest text that maps back to the same double.");
        System.out.println();

        // ---------- Task 3: 23.00 (zero cents) ----------
        double withoutCents = 23.00;

        System.out.println("Task 3 - dollar amount with zero cents");
        System.out.println("Stored value   : " + withoutCents);
        System.out.println("Exact double   : " + new BigDecimal(withoutCents));
        System.out.println("23.00 is a whole number and can be represented exactly,");
        System.out.println("so no rounding error appears (printed as 23.0).");
    }
}
