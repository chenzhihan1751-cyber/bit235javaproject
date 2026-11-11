/*
 * BIT235 Workshop 6 - Exercise 5 (Medium)
 *
 * Search engine: search an array of 10 paragraphs (from a book) for a
 * phrase and report which array index(es) contain it.
 *
 *  - phrase not found      -> print a "not found" message
 *  - phrase found          -> print the array index and the paragraph
 *
 * The search itself uses String.contains() as suggested in the hint. Both
 * sides are lower cased first so "Keyword Search" also matches, while the
 * paragraph that is printed keeps its original spelling.
 *
 * The phrases to look for are command line arguments, so the program can
 * search any phrase without being edited.
 */
public class ParagraphSearch {

    private static final String[] PARAGRAPHS = {
        "Lose all the weight you want.",
        "I can't I must work",
        "That would be like a keyword search.",
        "This would be Victoria.",
        "Join the party.",
        "To be or not to be.",
        "That is a question to test keyword search.",
        "Can you find a needle in a hay stack?",
        "This could be the last paragraph, but its not.",
        "Ada Lovelace is the worlds first programmer as of 1860."
    };

    /** Prints every paragraph that contains the phrase, or a not-found message. */
    private static void search(String phrase) {
        String needle = phrase.toLowerCase();
        int matches = 0;

        System.out.println("Phrase searched : \"" + phrase + "\"");
        for (int i = 0; i < PARAGRAPHS.length; i++) {
            if (PARAGRAPHS[i].toLowerCase().contains(needle)) {
                System.out.println("  index " + i + " : " + PARAGRAPHS[i]);
                matches++;
            }
        }
        if (matches == 0) {
            System.out.println("  Phrase not found in any of the "
                    + PARAGRAPHS.length + " paragraphs.");
        } else {
            System.out.println("  Matches found: " + matches);
        }
        System.out.println();
    }

    public static void main(String[] args) {

        System.out.println("Search engine over " + PARAGRAPHS.length + " paragraphs");
        System.out.println("==============================================");

        if (args.length == 0) {
            search("keyword search");     // default phrase
            search("needle");             // second example
            search("banana");             // example that is not there
        } else {
            for (int i = 0; i < args.length; i++) {
                search(args[i]);
            }
        }
    }
}
