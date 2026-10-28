/*
 * BIT235 Workshop 3 - Part 2
 * Explicit casting (narrowing conversion) using the USA national debt.
 *
 * Approximate US national debt (2026): about 38 trillion US dollars,
 * that is 38,000,000,000,000 dollars.
 *
 * long -> int keeps only the lowest 32 bits, so the value wraps around.
 * double -> byte first saturates to int, then keeps the lowest 8 bits.
 */
public class NationalDebt {
    public static void main(String[] args) {
        long debtLong = 38_000_000_000_000L;

        // 1) long -> int  (int only has 32 bits, so the high bits are lost)
        int debtInt = (int) debtLong;

        System.out.println("US national debt as a long : " + debtLong);
        System.out.println("US national debt as an int : " + debtInt);
        System.out.println("Did the value change?      : " + (debtInt != debtLong));
        System.out.println("Why: an int keeps only the lowest 32 bits, so the");
        System.out.println("value 38,000,000,000,000 wraps around to a negative int.");
        System.out.println();

        // 2) double -> byte (byte only keeps the lowest 8 bits)
        double debtDouble = 38_000_000_000_000.0;
        byte debtByte = (byte) debtDouble;

        System.out.println("US national debt as a double : " + debtDouble);
        System.out.println("US national debt as a byte   : " + debtByte);
        System.out.println("Did the value change?        : "
                + (debtByte != debtDouble));
        System.out.println("Why: the double is far outside the byte range, so it is");
        System.out.println("first clamped to Integer.MAX_VALUE and only the lowest");
        System.out.println("8 bits survive, which gives -1.");
    }
}
