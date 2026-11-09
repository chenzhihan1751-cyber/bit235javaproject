import java.util.ArrayList;

/**
 * Workshop Extension (OOP Concepts Extension PDF, page 2): central controller.
 *
 * This is the starter code from the sheet. It stores enclosures, assigns keepers
 * and prints a report.
 */
public class EnclosureManager {

    private ArrayList<Enclosure> enclosures;

    public EnclosureManager() {
        enclosures = new ArrayList<Enclosure>();
    }

    public void addEnclosure(Enclosure e) {
        enclosures.add(e);
    }

    public void assignKeeperToEnclosure(int index, ZooKeeper k) {
        if (index >= 0 && index < enclosures.size()) {
            enclosures.get(index).assignKeeper(k);
        }
    }

    public void printReport() {
        for (Enclosure e : enclosures) {
            e.displayDetails();
            System.out.println("----------------------");
        }
    }

    // Small extra helper so the report can also show the size of the collection.
    public int getEnclosureCount() {
        return enclosures.size();
    }
}
