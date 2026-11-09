/**
 * OOP Concepts Workshop, step 9: an Aviary is an Enclosure (inheritance).
 */
public class Aviary extends Enclosure {

    private double flightHeightM;

    public Aviary(String enclosureId, int capacity, double flightHeightM) {
        super(enclosureId, capacity);
        this.flightHeightM = flightHeightM;
    }

    public double getFlightHeightM() {
        return flightHeightM;
    }

    @Override
    public String getType() {
        return "Aviary";
    }

    @Override
    public void displayDetails() {
        super.displayDetails();
        System.out.println("Flight height: " + flightHeightM + " m");
    }
}
