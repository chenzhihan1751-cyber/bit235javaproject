/**
 * OOP Concepts Workshop, step 9: an Aquarium is an Enclosure (inheritance).
 */
public class Aquarium extends Enclosure {

    private String waterType;
    private double depthM;

    public Aquarium(String enclosureId, int capacity, String waterType, double depthM) {
        super(enclosureId, capacity);
        this.waterType = waterType;
        this.depthM = depthM;
    }

    public String getWaterType() {
        return waterType;
    }

    public double getDepthM() {
        return depthM;
    }

    @Override
    public String getType() {
        return "Aquarium";
    }

    @Override
    public void displayDetails() {
        super.displayDetails();
        System.out.println("Water type   : " + waterType);
        System.out.println("Depth        : " + depthM + " m");
    }
}
