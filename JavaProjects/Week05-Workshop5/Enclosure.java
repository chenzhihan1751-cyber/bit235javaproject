/**
 * OOP Concepts Workshop, steps 4-5.
 *
 * Step 4: new field ZooKeeper keeper and method assignKeeper(ZooKeeper k).
 * Step 5: displayDetails() prints the enclosure id, the capacity and the name of
 *         the assigned keeper (keeper.givenName + keeper.familyName).
 *
 * Cage, Aquarium and Aviary extend this class, so a variable of type Enclosure
 * can hold any of them (steps 12-16).
 */
public class Enclosure {

    private String enclosureId;
    private int capacity;

    // Step 4: the keeper who looks after this enclosure.
    private ZooKeeper keeper;

    public Enclosure(String enclosureId, int capacity) {
        this.enclosureId = enclosureId;
        this.capacity = capacity;
    }

    public String getEnclosureId() {
        return enclosureId;
    }

    public int getCapacity() {
        return capacity;
    }

    public ZooKeeper getKeeper() {
        return keeper;
    }

    // Step 4: assign the keeper to this enclosure. The link is kept on both
    // sides so that ZooKeeper.displayEnclosures() can list the same relationship.
    public void assignKeeper(ZooKeeper k) {
        if (keeper != null && keeper != k) {
            keeper.removeEnclosure(this);
        }
        this.keeper = k;
        if (k != null && k.getEnclosures().indexOf(this) < 0) {
            k.assignEnclosure(this);
        }
    }

    // Overridden by the subclasses; used only when printing.
    public String getType() {
        return "Enclosure";
    }

    // Step 5: id, capacity and the assigned keeper's name.
    public void displayDetails() {
        System.out.println("Type         : " + getType());
        System.out.println("Enclosure ID : " + enclosureId);
        System.out.println("Capacity     : " + capacity);
        if (keeper == null) {
            System.out.println("ZooKeeper    : (not assigned)");
        } else {
            System.out.println("ZooKeeper    : "
                    + keeper.getGivenName() + " " + keeper.getFamilyName());
        }
    }
}
