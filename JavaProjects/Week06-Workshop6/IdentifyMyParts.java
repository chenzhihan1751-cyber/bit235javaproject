/*
 * BIT235 Workshop 6 - Exercise 6 (Easy) - part 1 of 2
 *
 * The class from the question, unchanged:
 *
 *   public class IdentifyMyParts {
 *       public static int x = 7;
 *       public int y = 3;
 *   }
 *
 * x is a CLASS variable (static): one copy exists for the whole class,
 *   shared by every object and reachable as IdentifyMyParts.x.
 * y is an INSTANCE variable (no static): every object made with "new"
 *   gets its own copy, so a.y and b.y are two different fields.
 *
 * IdentifyPartsDemo runs the code from the question to prove the answer.
 */
public class IdentifyMyParts {

    public static int x = 7;   // class variable - shared by all objects
    public int y = 3;          // instance variable - one per object
}
