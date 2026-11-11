/*
 * BIT235 Workshop 6 - Exercise 4 (Easy)
 *
 * Decode a coded message with the substitution key given in the question.
 *
 * The key (a -> c, b -> r, c -> g, ... z -> t) is stored as one String:
 *   CODE_ALPHABET  = "abcdefghijklmnopqrstuvwxyz"   (the coded letter)
 *   PLAIN_ALPHABET = "crgzavibsdoeqfhujxklwmynpt"   (what it decodes to)
 * The letter at position i in CODE_ALPHABET decodes to the letter at
 * position i in PLAIN_ALPHABET, so decoding is just indexOf + charAt.
 *
 * Nothing about "G tgsl Qefe." is hard coded in the decoding loop, so a
 * different message only needs a different String in main().
 */
public class DecodeMessage {

    private static final String CODE_ALPHABET  = "abcdefghijklmnopqrstuvwxyz";
    private static final String PLAIN_ALPHABET = "crgzavibsdoeqfhujxklwmynpt";

    /** Decodes one coded letter, keeping the original upper/lower case. */
    private static char decodeChar(char coded) {
        char lower = Character.toLowerCase(coded);
        int position = CODE_ALPHABET.indexOf(lower);
        if (position < 0) {
            return coded;              // not a letter: space, dot, digit...
        }
        char plain = PLAIN_ALPHABET.charAt(position);
        if (Character.isUpperCase(coded)) {
            plain = Character.toUpperCase(plain);
        }
        return plain;
    }

    /** Decodes a whole message. */
    private static String decode(String message) {
        char[] chars = message.toCharArray();
        char[] result = new char[chars.length];
        for (int i = 0; i < chars.length; i++) {
            result[i] = decodeChar(chars[i]);
        }
        return new String(result);
    }

    public static void main(String[] args) {

        String coded = "G tgsl Qefe.";
        if (args.length > 0) {
            StringBuffer joined = new StringBuffer();
            for (int i = 0; i < args.length; i++) {
                if (i > 0) {
                    joined.append(' ');
                }
                joined.append(args[i]);
            }
            coded = joined.toString();
        }

        System.out.println("Substitution key used for decoding");
        System.out.println("  coded : " + CODE_ALPHABET);
        System.out.println("  plain : " + PLAIN_ALPHABET);
        System.out.println();
        System.out.println("Coded message   : " + coded);
        System.out.println("Decoded message : " + decode(coded));
    }
}
