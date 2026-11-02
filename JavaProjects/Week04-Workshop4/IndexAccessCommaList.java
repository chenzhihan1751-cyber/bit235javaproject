/*
 * BIT235 Object Oriented Programming - Week 4
 * Arrays exercise, Q8: printing the people array as a comma separated line
 * with no comma after the last value.
 */
public class IndexAccessCommaList {

    public static void main(String[] args) {
        String[] people = {"Wilma", "Fred", "Barney", "Betty", "Pebbles"};

        StringBuilder line = new StringBuilder();
        boolean first = true;
        for (String person : people) {
            if (!first) {
                line.append(", ");   // separator goes before every item but the first
            }
            line.append(person);
            first = false;
        }

        System.out.println(line);
    }
}
