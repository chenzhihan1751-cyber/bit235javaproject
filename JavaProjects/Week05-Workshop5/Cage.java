/**
 * OOP Concepts Workshop, step 9: a Cage is an Enclosure (inheritance).
 * It adds its own field and overrides displayDetails() to show it, while still
 * calling super.displayDetails() for the shared fields.
 */
public class Cage extends Enclosure {

    private double meshSizeMm;

    public Cage(String enclosureId, int capacity, double meshSizeMm) {
        super(enclosureId, capacity);
        this.meshSizeMm = meshSizeMm;
    }

    public double getMeshSizeMm() {
        return meshSizeMm;
    }

    @Override
    public String getType() {
        return "Cage";
    }

    @Override
    public void displayDetails() {
        super.displayDetails();
        System.out.println("Mesh size    : " + meshSizeMm + " mm");
    }
}
