import java.util.ArrayList;

/**
 * OOP Concepts Workshop, steps 1-3 and 17-20.
 *
 * Steps 1-3  : id, givenName and familyName fields plus displayDetails().
 * Steps 17-20: a keeper can be assigned to more than one enclosure, so the class
 *              keeps an ArrayList<Enclosure> and offers assignEnclosure().
 */
public class ZooKeeper {

    private int id;
    private String givenName;
    private String familyName;

    // Step 17: one keeper, many enclosures.
    private ArrayList<Enclosure> enclosures;

    public ZooKeeper(int id, String givenName, String familyName) {
        this.id = id;
        this.givenName = givenName;
        this.familyName = familyName;
        this.enclosures = new ArrayList<Enclosure>();
    }

    public int getId() {
        return id;
    }

    public String getGivenName() {
        return givenName;
    }

    public String getFamilyName() {
        return familyName;
    }

    public String getFullName() {
        return givenName + " " + familyName;
    }

    public ArrayList<Enclosure> getEnclosures() {
        return enclosures;
    }

    // Step 2: print the keeper's details.
    public void displayDetails() {
        System.out.println("ZooKeeper ID : " + id);
        System.out.println("ZooKeeper    : " + getFullName());
    }

    // Step 18: assign one more enclosure to this keeper.
    public void assignEnclosure(Enclosure e) {
        if (e == null) {
            return;
        }
        if (!enclosures.contains(e)) {
            enclosures.add(e);
        }
        // Keep both sides of the relationship in step: the enclosure also needs
        // to know its keeper, otherwise Enclosure.displayDetails() shows "none".
        if (e.getKeeper() != this) {
            e.assignKeeper(this);
        }
    }

    public void removeEnclosure(Enclosure e) {
        enclosures.remove(e);
    }

    // Step 20: list every enclosure this keeper is responsible for.
    public void displayEnclosures() {
        System.out.println("Enclosures managed by " + getFullName() + ":");
        if (enclosures.isEmpty()) {
            System.out.println("  (none)");
            return;
        }
        for (Enclosure e : enclosures) {
            System.out.println("  - " + e.getEnclosureId()
                    + " (" + e.getType() + ", capacity " + e.getCapacity() + ")");
        }
    }
}
