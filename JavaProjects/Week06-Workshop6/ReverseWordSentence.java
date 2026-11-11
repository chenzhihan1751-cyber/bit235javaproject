/*
 * BIT235 Workshop 6 - Exercise 3 (Medium)
 *
 * Reverse the sequence of letters inside every word of a sentence,
 * using only loop(s) and array(s) - no String.split(), no StringBuilder.
 *
 * "To be or not to be."  ->  "oT eb ro ton ot eb."
 *
 * Method: copy the sentence into a char[] array, then walk it with two
 * indexes. Every run of letters/digits is one word; the word is reversed
 * in place by swapping its first and last char and moving inwards.
 * Spaces and punctuation stay exactly where they are.
 */
public class ReverseWordSentence {

    /** Reverses chars from index start to index end (inclusive), in place. */
    private static void reverseRange(char[] letters, int start, int end) {
        int left = start;
        int right = end;
        while (left < right) {
            char tmp = letters[left];
            letters[left] = letters[right];
            letters[right] = tmp;
            left++;
            right--;
        }
    }

    public static void main(String[] args) {

        // Allow a different sentence on the command line, default is the
        // one from the workshop question.
        String sentence;
        if (args.length > 0) {
            StringBuffer joined = new StringBuffer();
            for (int i = 0; i < args.length; i++) {
                if (i > 0) {
                    joined.append(' ');
                }
                joined.append(args[i]);
            }
            sentence = joined.toString();
        } else {
            sentence = "To be or not to be.";
        }

        char[] letters = sentence.toCharArray();

        int i = 0;
        int wordCount = 0;
        while (i < letters.length) {
            if (Character.isLetterOrDigit(letters[i])) {
                int start = i;
                while (i < letters.length && Character.isLetterOrDigit(letters[i])) {
                    i++;
                }
                reverseRange(letters, start, i - 1);   // end is i-1 == last letter
                wordCount++;
            } else {
                i++;                                   // space or punctuation
            }
        }

        String reversed = new String(letters);

        System.out.println("Original sentence : " + sentence);
        System.out.println("Words reversed    : " + reversed);
        System.out.println("Words processed   : " + wordCount);
    }
}
